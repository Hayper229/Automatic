import os
import time
import colorama as cn
cn.init(autoreset=True)
def main():
    print(f'{cn.Fore.YELLOW}Starting in..{cn.Fore.GREEN}[{cn.Fore.WHITE}{time.asctime()}{cn.Fore.GREEN}]\n{cn.Fore.GREEN+"_"*50}')
    for site in os.listdir('/root/.local/share/sqlmap/output/'):
        if site.endswith('.csv'):
           pass
        else:
            print(f'{cn.Fore.YELLOW}{site}')
            pass
    print(f'{cn.Fore.YELLOW}Ending in..{cn.Fore.GREEN}[{cn.Fore.WHITE}{time.asctime()}{cn.Fore.GREEN}]\n{cn.Fore.GREEN+"_"*50}')



if __name__ == "__main__":
   main()
