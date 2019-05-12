# author: Mahmud Ahsan
# code: https://github.com/mahmudahsan/thinkdiff
# blog: http://thinkdiff.net
# http://pythonbangla.com
# MIT License

# --------------------------
#  Download Concurrently
#  By concurrent.futures 
# --------------------------

# A process is an executing program
# A thread is the basic unit for that operating system allocates processor time. A process can have multiple threads.

from concurrent import futures 

from download_serial import save_image, download_image
from download_serial import debug_msg, saving_file_name, main

# Maximum number of thread used in ThreadPoolExecutor
MAX_THREAD = 50

def download_single(country):
    image = download_image(country)
    debug_msg(country)
    save_image(image, saving_file_name(country))
    return country
    
def download_all_concurr1(countries):
    threads = min(MAX_THREAD, len(countries))
     
    with futures.ThreadPoolExecutor(threads) as executor:
        response = executor.map(download_single, countries)
        
    return len(list(response))
    
if __name__ == '__main__':
    main(download_all_concurr1)