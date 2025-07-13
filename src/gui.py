import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import io
from PIL import Image, ImageTk
from .converter import convert_to_avif
from .utils import load_settings, save_settings

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ガゾーヘンカン (GazoHenkan)")
        self.geometry("600x450")
        
        self.file_list = []
        self.output_dir = tk.StringVar()
        self.lossless_var = tk.BooleanVar()
        
        self.create_widgets()
        self.load_and_apply_settings()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = ttk.Label(main_frame, text="ガゾーヘンカン (GazoHenkan)", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 10))
        
        # File list section
        list_frame = ttk.LabelFrame(main_frame, text="変換ファイル一覧")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # File listbox with scrollbar
        listbox_frame = ttk.Frame(list_frame)
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.listbox = tk.Listbox(listbox_frame)
        scrollbar = ttk.Scrollbar(listbox_frame)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # File buttons
        file_buttons_frame = ttk.Frame(list_frame)
        file_buttons_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(file_buttons_frame, text="ファイル追加", 
                  command=self.add_files).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(file_buttons_frame, text="フォルダ追加", 
                  command=self.add_folder).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(file_buttons_frame, text="リストをクリア", 
                  command=self.clear_list).pack(side=tk.LEFT)
        
        # Settings section
        settings_frame = ttk.LabelFrame(main_frame, text="変換設定")
        settings_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Quality setting
        quality_frame = ttk.Frame(settings_frame)
        quality_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(quality_frame, text="品質:").pack(side=tk.LEFT)
        self.quality_scale = tk.Scale(quality_frame, from_=10, to=100, 
                                     orient=tk.HORIZONTAL, length=200)
        self.quality_scale.set(80)
        self.quality_scale.pack(side=tk.LEFT, padx=(5, 10))
        
        self.quality_label = ttk.Label(quality_frame, text="80")
        self.quality_label.pack(side=tk.LEFT)
        self.quality_scale.config(command=self.update_quality_label)
        
        # Lossless setting
        ttk.Checkbutton(settings_frame, text="ロスレス変換", 
                       variable=self.lossless_var).pack(anchor=tk.W, padx=5, pady=5)
        
        # Output directory setting
        output_frame = ttk.Frame(settings_frame)
        output_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(output_frame, text="出力フォルダ:").pack(side=tk.LEFT)
        ttk.Entry(output_frame, textvariable=self.output_dir, state="readonly").pack(
            side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 5))
        ttk.Button(output_frame, text="選択", 
                  command=self.select_output_dir).pack(side=tk.RIGHT)
        
        # Action buttons
        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(action_frame, text="プレビュー", 
                  command=self.show_preview).pack(side=tk.RIGHT, padx=(5, 0))
        self.convert_button = ttk.Button(action_frame, text="変換開始", 
                                        command=self.start_conversion_thread)
        self.convert_button.pack(side=tk.RIGHT, padx=(5, 5))
        
        # Progress section
        progress_frame = ttk.Frame(main_frame)
        progress_frame.pack(fill=tk.X)
        
        self.progress_bar = ttk.Progressbar(progress_frame)
        self.progress_bar.pack(fill=tk.X, pady=(0, 5))
        
        self.status_label = ttk.Label(progress_frame, text="準備完了")
        self.status_label.pack(anchor=tk.W)

    def update_quality_label(self, value):
        self.quality_label.config(text=str(int(float(value))))

    def add_files(self):
        file_types = [
            ("画像ファイル", "*.jpg *.jpeg *.png"),
            ("JPEGファイル", "*.jpg *.jpeg"),
            ("PNGファイル", "*.png"),
            ("すべてのファイル", "*.*")
        ]
        files = filedialog.askopenfilenames(
            title="変換するファイルを選択",
            filetypes=file_types
        )
        
        for file_path in files:
            if self.is_supported_file(file_path):
                if file_path not in self.file_list:
                    self.file_list.append(file_path)
                    self.listbox.insert(tk.END, os.path.basename(file_path))
            else:
                messagebox.showwarning("警告", 
                    f"サポートされていないファイル形式です: {os.path.basename(file_path)}")
        
        self.update_status()

    def add_folder(self):
        folder_path = filedialog.askdirectory(title="フォルダを選択")
        if folder_path:
            added_count = 0
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if self.is_supported_file(file_path):
                        if file_path not in self.file_list:
                            self.file_list.append(file_path)
                            self.listbox.insert(tk.END, os.path.basename(file_path))
                            added_count += 1
            
            if added_count > 0:
                self.status_label.config(text=f"{added_count}個のファイルを追加しました")
            else:
                messagebox.showinfo("情報", "対応ファイルが見つかりませんでした")
            
            self.update_status()

    def is_supported_file(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        return ext in ['.jpg', '.jpeg', '.png']

    def clear_list(self):
        self.listbox.delete(0, tk.END)
        self.file_list.clear()
        self.status_label.config(text="リストがクリアされました")

    def select_output_dir(self):
        folder = filedialog.askdirectory(title="出力フォルダを選択")
        if folder:
            self.output_dir.set(folder)

    def show_preview(self):
        selected_indices = self.listbox.curselection()
        if not selected_indices:
            messagebox.showinfo("情報", "プレビューするファイルを選択してください")
            return
        
        file_path = self.file_list[selected_indices[0]]
        quality = int(self.quality_scale.get())
        lossless = self.lossless_var.get()
        
        try:
            # Create preview window
            preview_win = tk.Toplevel(self)
            preview_win.title("プレビュー")
            preview_win.geometry("800x600")
            
            # Original Image
            original_img = Image.open(file_path)
            original_size = os.path.getsize(file_path)
            original_img.thumbnail((380, 380))
            original_photo = ImageTk.PhotoImage(original_img)
            
            left_frame = ttk.Frame(preview_win)
            left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
            ttk.Label(left_frame, image=original_photo).pack()
            ttk.Label(left_frame, text=f"オリジナル: {os.path.basename(file_path)}").pack()
            ttk.Label(left_frame, text=f"サイズ: {original_size / 1024:.2f} KB").pack()
            
            # Converted Image (in memory)
            converted_img_data = io.BytesIO()
            original_img_for_conversion = Image.open(file_path)
            
            # Check if AVIF format is supported
            print(f"Available formats: {Image.registered_extensions()}")
            if '.avif' not in Image.registered_extensions():
                raise Exception("AVIF format not supported. Please install pillow-avif-plugin.")
            
            original_img_for_conversion.save(converted_img_data, "AVIF", 
                                           quality=quality, lossless=lossless)
            converted_size = converted_img_data.tell()
            converted_img_data.seek(0)
            converted_img = Image.open(converted_img_data)
            converted_img.thumbnail((380, 380))
            converted_photo = ImageTk.PhotoImage(converted_img)
            
            right_frame = ttk.Frame(preview_win)
            right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
            ttk.Label(right_frame, image=converted_photo).pack()
            ttk.Label(right_frame, text="変換後 (AVIF)").pack()
            ttk.Label(right_frame, text=f"サイズ: {converted_size / 1024:.2f} KB").pack()
            
            # Compression Info
            reduction = (1 - converted_size / original_size) * 100 if original_size > 0 else 0
            ttk.Label(preview_win, text=f"圧縮率: {reduction:.2f}% 削減", 
                     font=("Arial", 12)).pack(side=tk.BOTTOM, pady=10)
            
            # Keep references to prevent garbage collection
            left_frame.image = original_photo
            right_frame.image = converted_photo
            
        except Exception as e:
            messagebox.showerror("プレビューエラー", 
                f"プレビューの生成中にエラーが発生しました\n{e}")

    def start_conversion_thread(self):
        if not self.file_list:
            messagebox.showwarning("警告", "変換するファイルがありません")
            return
        
        if not self.output_dir.get():
            messagebox.showwarning("警告", "出力フォルダを選択してください")
            return
        
        # Start conversion in separate thread
        thread = threading.Thread(target=self.convert_files)
        thread.daemon = True
        thread.start()

    def convert_files(self):
        try:
            self.convert_button.config(state="disabled")
            total_files = len(self.file_list)
            self.progress_bar.config(maximum=total_files)
            
            output_folder = self.output_dir.get()
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            quality = int(self.quality_scale.get())
            lossless = self.lossless_var.get()
            
            for i, file_path in enumerate(self.file_list):
                try:
                    self.status_label.config(text=f"変換中: {os.path.basename(file_path)}")
                    
                    output_path = os.path.join(output_folder, 
                        os.path.splitext(os.path.basename(file_path))[0] + ".avif")
                    
                    convert_to_avif(file_path, output_path, quality, lossless)
                    
                    self.progress_bar.config(value=i + 1)
                    self.status_label.config(text=f"完了: {i + 1}/{total_files}")
                    
                except Exception as e:
                    print(f"Error converting {file_path}: {e}")
                    continue
            
            self.status_label.config(text=f"変換完了: {total_files}ファイル")
            messagebox.showinfo("完了", f"{total_files}ファイルの変換が完了しました")
            
        except Exception as e:
            messagebox.showerror("エラー", f"変換中にエラーが発生しました\n{e}")
        
        finally:
            self.convert_button.config(state="normal")
            self.progress_bar.config(value=0)

    def update_status(self):
        count = len(self.file_list)
        if count == 0:
            self.status_label.config(text="準備完了")
        else:
            self.status_label.config(text=f"{count}ファイルが選択されています")

    def load_and_apply_settings(self):
        settings = load_settings()
        self.quality_scale.set(settings.get('quality', 80))
        self.lossless_var.set(settings.get('lossless', False))
        output_dir = settings.get('output_directory', 'output')
        self.output_dir.set(output_dir)
        self.update_quality_label(self.quality_scale.get())

    def on_closing(self):
        settings_to_save = {
            'quality': int(self.quality_scale.get()),
            'lossless': self.lossless_var.get(),
            'output_directory': self.output_dir.get()
        }
        save_settings(settings_to_save)
        self.destroy()

if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()