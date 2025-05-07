import os
import shutil
import webbrowser
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

#版本：1.1.1.0 beta
#作者：昭诗雨
# 创建主窗口
root = tk.Tk()
root.title("康熙启动器(客户端)")
root.geometry("1200x600")  # 设置窗口大小
root.configure(bg="gray")
#root.iconbitmap(r'Example/favicon.ico')  # 设置主窗口图标
root.iconphoto(True, tk.PhotoImage(file='data/Example/favicon.ico'))
# 加载背景图片
background_image = Image.open(r"data/Example/a.jpg")  # 替换为你的图片路径
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.geometry(f"{background_image.width}x{background_image.height}")


# 帮助菜单内容
#设置
#路径
def show_lujing():
    # 打开文件选择对话框
    file_path = filedialog.askdirectory(title="请选择原神所在文件夹")
    with open("path.txt", "w", encoding="utf-8") as file:
        file.write(file_path)
#帮助
def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("帮助")
    help_window.geometry("350x500")  # 设置弹窗大小
    root.iconphoto(True, tk.PhotoImage(file='data/Example/favicon.ico'))
    help_text = """
    欢迎使用康熙启动器！

    1. 输入原神路径：
       - 在‘设置’菜单栏打开“原神路径”选项
       - 在弹出的命令窗口中选中原神启动程序“YuanShen.exe”
       - 点击确定

    2. 启动原神：
       - 根据需要在首页面板点击“原神官方版”或“原神私服版”

    如果您有任何问题，请联系我们的客服团队。
    """
    label = tk.Label(help_window, text=help_text, justify="left", padx=10, pady=10)
    label.pack(fill="both", expand=True)

#官网
# 官网
def open_guanwang():
    webbrowser.open("https://zhan.kangxidi.shop/")
#康熙盘
def open_pan():
    webbrowser.open("https://pan.kangxidi.shop/")
#github
def open_github():
    webbrowser.open("https://github.com/woailulu/GenshinImpact-PrivateService-zuizhong")
#百度
def open_baidu():
    webbrowser.open("https://www.baidu.com")


#功能
#寻找“YuanShen.exe文件”
def find_yuanshen_exe():
    try:
        with open("path.txt", "r", encoding="utf-8") as file:
            lujing = file.read().strip()

        target_names = ["YuanShen.exe", "GenshinImpact.exe"]  # 修改为支持多个目标文件名

        for root, dirs, files in os.walk(lujing):
            for target_name in target_names:  # 遍历目标文件名列表
                if target_name in files:  # 检查文件
                    return os.path.join(root, target_name)
                elif target_name in dirs:  # 检查文件夹
                    return os.path.join(root, target_name)
        return None
    except Exception as e:
        messagebox.showerror("错误", f"读取路径时出错：{e}", icon="error")
        return None
#官服
def open_yuanshen_guanfu():
    yuanshen_exe = find_yuanshen_exe()
    if yuanshen_exe and os.path.exists(yuanshen_exe):
        os.startfile(yuanshen_exe)  # 启动原神
        messagebox.showinfo("提示", "原神官方版开启成功", icon="info")
    else:
        messagebox.showerror("错误", "未找到原神官方版路径，请检查设置", icon="error")

#私服
#第一步
def open_yuanshen_sifu():
    with open("path.txt", "r", encoding="utf-8") as file:
        lujing = file.read().strip()
    source_folder = r"data\Patch" # 替换为源文件夹路径
    file_to_copy  = "version.dll"
    file_to_copy1 = "version.json"
    source_file_path1 = os.path.join(source_folder, file_to_copy)
    source_file_path = os.path.join(source_folder, file_to_copy1)
    destination_file_path1 = os.path.join(lujing, file_to_copy)
    destination_file_path = os.path.join(lujing, file_to_copy1)
    try:
        shutil.copy(source_file_path1, destination_file_path1)
        shutil.copy(source_file_path, destination_file_path)
    except Exception as e:
        messagebox.showerror("错误", f"文件复制失败：{e}", icon="error")
    os.startfile(r"data\GcTools\GcTools.exe")
    help_window = tk.Toplevel(root)
    help_window.title("教程")
    help_window.geometry("350x500")  # 设置弹窗大小
    root.iconphoto(True, tk.PhotoImage(file='data/Example/favicon.ico'))
    help_text = """
    欢迎使用康熙启动器！
        - 在割草机工具(GrasscutterTools)中选择"代理"
        - 点击“启动代理”按钮
        - 在代理启动后点击本页“确定”按钮
    """
    label = tk.Label(help_window, text=help_text, justify="left", padx=10, pady=10)
    label.pack(fill="both", expand=True)
    confirm_button = tk.Button(help_window, text="确定", command=open_sifu)
    confirm_button.pack(pady=20)
#第二步
def open_sifu():
    result = find_yuanshen_exe()  # 调用查找函数
    os.startfile(result)  # 打开指定路径的程序或文件
    # 弹出消息框
    messagebox.showinfo("提示", "原神私服开启成功", icon="info")







# 创建菜单栏
menubar = tk.Menu(root)
# 添加“设置”菜单
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label="原神路径", command=show_lujing)
settings_menu.add_command(label="查看帮助", command=show_help)
settings_menu.add_separator()  # 添加分隔线
settings_menu.add_command(label="退出", command=root.quit)
# 添加“官网”菜单
guanwang_menu = tk.Menu(menubar, tearoff=0)
guanwang_menu.add_command(label="官网", command=open_guanwang)
guanwang_menu.add_command(label="康熙盘", command=open_pan)
guanwang_menu.add_command(label="github", command=open_github)
guanwang_menu.add_command(label="百度", command=open_baidu)
# 将菜单添加到菜单栏
menubar.add_cascade(label="设置", menu=settings_menu)
menubar.add_cascade(label="官网", menu=guanwang_menu)

# 创建按钮
#官服
yuanmiuishe = tk.Button(root, text="原神官方版", command=open_yuanshen_guanfu, bg="gray", fg="white", width=10, height=2)
yuanmiuishe.place(relx=0.2, rely=0.9, anchor="sw")
#私服
yuansifu = tk.Button(root, text="原神私服版", command=open_yuanshen_sifu, bg="gray", fg="white", width=10, height=2)
yuansifu.place(relx=0.8, rely=0.9, anchor="se")

# 配置主窗口使用菜单栏
root.config(menu=menubar)
# 运行主循环
root.mainloop()