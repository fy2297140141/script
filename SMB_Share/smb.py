### smb共享版

import os
import sys
import xlrd

# 读取用户数据表
def read_xlsx(path):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)
    hang = int(table.nrows)
    lie = int(table.ncols)
    list_ls = [] 
    for i in range(hang):
        dic = {"name":"null","password":"null","group":"null"}
        dic["name"] = str(table.cell_value(i,0))
        dic["password"] = str(table.cell_value(i,1))
        dic["group"] = str(table.cell_value(i,2))
        list_ls.append(dic)
    return list_ls


# 创建用户
def creat(user, password):
    # net user username password /add   cmd添加用户命令
    command = "net user %s %s /add" %(user, password)
    os.system(command)

# 设置隶属组 
def set_group(user, group):
    # net localgroup groupname username /add   cmd添加用户进组命令
    command1 = "net localgroup %s %s /add" %(group, user)
    os.system(command1)
    # net localgroup groupname username /del   cmd将用户从组中删除命令
    command2 = "net localgroup Users %s /del" %(user)
    os.system(command2)

# 创建用户文件夹及设置权限
def creat_file(file_dict):
    for i in file_dict:
        name = i["name"]
        # md d:\share\student1    cmd新建文件夹命令
        command1 = "md d:\share\%s" %(name)
        os.system(command1)
        # 用户权限
        command2 = "Cacls d:\share\%s /t /e /c /g %s:F" %(name, name)
        os.system(command2)

# 设置主文件夹共享
def share_file():
    print("请输入共享名称", end=' ')
    file_name = input()
    command = "net share %s=d:\share" %(file_name)
    os.system(command)


# 主函数
def main(file_path):
    user_dict = read_xlsx(file_path) # 用户列表
    for i in user_dict:
        username = i["name"]
        password = i["password"]
        groupname = i["group"]
        # 创建用户
        creat(username, password)
        # 设置用户隶属组
        set_group(username,groupname)
    # 创建用户文件夹
    command = "md d:\share"
    os.system(command)
    tip(user_dict)    
    share_file()

# 手动操作提示
def tip(user_dict):
    print("请手动设置文件权限，设置完成后再继续操作！！（Y/N）：", end=' ')
    check_flag = input()
    if check_flag == "y" or check_flag == "Y":
        creat_file(user_dict)



print("\t自动创建用户脚本（SMB版）")
print("温馨提示：使用前请检查杀毒软件是否关闭。（Y/N）：",end=' ')
flag = input()
if flag == "Y" or flag == "y" :
    print("是否需要新建用户组？（Y/N）：",end=' ')
    flag1 = input()
    if flag1 == "Y" or flag1 =="y":
        print("请输入要新建的用户组名称：(需于excel文件内的用户组名称一致)：",end=' ')
        flag2 = input()
        command = "net localgroup %s /add" %(flag2)
        os.system(command)
    print("输入用户表路径：")
    path = input()
    main(path)
else:
    print("请关闭杀毒软件后再次打开此脚本")
    print("脚本结束")
    sys.exit(0)





    
