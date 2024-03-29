from config.data import urls, time_altered
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import traceback
import requests
import logging

class parser:
        @staticmethod
        def main():
            try:
                print('Loading...')
                time_altered.time_buffer(1)
                print("""
                    ////////  W I L L C A T O N J R /////////
                    ----------------------------------------
                      SUBDOMAIN - SUBDIRECTORY ENUMERATION
                    """)
                with open(f'subdomains.csv', 'w') as file:
                    for url in urls.url_list: 
                        try:
                            value = urls.url_list[0]
                            response = requests.get(value)
                            response.raise_for_status()
                            soup = BeautifulSoup(response.content, 'html.parser')
                            for link in soup.findAll('a'):
                                    file.writelines(link.get('href') + '\n'+ '\n')
                            file.close()
                            break
                        except HTTPError as err:
                            logging.error(f"Failed to fetch URL: {url}, Error: {err}")
            except Exception as err:
                logging.error(err)
                traceback.print_exc(limit=None,file=None,chain=True)

if __name__ == "__main__":
    func = parser()
    func.main()
    print('Finished')

# ISSUE:
    # THE URLs OUTPUT 3 TIMES EACH FILE. 
# TRAIL FIXES:
    # IT'S NOT ATTACHED TO THE NUMBER OF EXECUTIONS - FOR LOOP - THAT WRAP THE VARIABLES INSIDE OF THE MAIN() FUNCTION.
    # --TRIED DELETING THE FOR LOOP
    # USING A BREAK STATEMENT ON THE NUMS EXECUTION FOR LOOP DIDNT WORK.
    # SLICING THE URL_DICT INDEX. THAT DIDN'T WORK.
    # I TRIED USING A FOR LOOP OUTSIDE OF THE CLASS WITH A GLOBAL VARIABLE ATTACHED TO THE (i) ITERATOR VARIABLE.
    #findall() function didnt work but the FindAll function does.
    # find() function doesn't work.
    # i+=1 incremetor didn't work.
# THOUGHTS:
    # THE ISSUE IS THE SUBDOMAINS ARE OUTPUTTING 3 TIMES TO EACH CSV FILE SO THE ISSUE MUST BE WITH THE WAY THE PROGEAM OUTPUTS. 
    # THAT'S WHY I THINK THE CORE ISSUE IS THE WITH OPEN() STATEMENT / FUNCTION. 
    # THE PROBLEM ISN'T THE FOR LOOP THAT FINDS THE HTML TAGS. BREAKING THE FOR LOOP IS WHAT I TRIED, BUT IT DIDN'T WORK.
    # THE i VARIABLE IS ITERATING OVER EACH URL 3 TIMES. THAT IS THE ISSUE. 
    # I TRIED PASSING THE URL ITERATOR TO THE VALUE VARIABLE. THAT DIDN'T WORK.
    # --OR INDEXING WITH IT. USING THE i ITERATOR OR PASSING THE URL ITERATOR IN THE EMPTY LIST AS WHEN INDEXING.
    # NESTING THE FINALL FOR LOOP IN A NUM_EXECUTIONS FOR LOOP DIDN'T WORK
    # file.close() has gotten me closer to the solution.