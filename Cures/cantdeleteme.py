def cantdeleteme_cure():
    import getpass as gp
    import platform as pf
    import os

    def get_user():
        try:
            ret = gp.getuser()
        except:
            try:
                if pf.system() == 'Darwin':
                    temp_list = os.getcwd().split('/')
                elif pf.system() == 'Windows':
                    temp_list = os.getcwd().split('\\')
                ret = temp_list [temp_list.index('Users') + 1]
            except:
                try:
                    if pf.system() == 'Darwin':
                        temp_list = __file__.split('/')
                    elif pf.system() == 'Windows':
                        temp_list = __file__.split('\\')
                    ret = temp_list [temp_list.index('Users') + 1]
                except:
                    ret = 'Unable to determine'
        return ret

    os.remove(f'C:\\Users\\{get_user()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bootup_processes.vbs')



if __name__ == '__main__':
    cantdeleteme_cure()
