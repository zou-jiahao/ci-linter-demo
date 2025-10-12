# main.py - 故意违反 PEP8 规范
def  say_hello ( name ) :  # 多余空格，缺少空行
    print(f"Hello, {name}! This is a very long line that exceeds the recommended 79 characters limit and should trigger a warning in flake8.........................................")
 
say_hello ( "World" )  # 多余空格
