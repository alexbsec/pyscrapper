import argparse
from imports import googleScrapper
from simple_chalk import chalk

def main():
    # Define the command-line arguments
    parser = argparse.ArgumentParser(description="Scrape Google search results.")
    parser.add_argument("query", help="the search query", nargs="+")
    parser.add_argument("-b", "--brute-search", action="store_true", help="perform a brute-force search")
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")
    parser.add_argument("-f", "--filetype", help="search for a specific file type")
    parser.add_argument("-s", "--site", help="search for results from a specific website")
    parser.add_argument("-d", "--delay", help="delay between requests")
    parser.add_argument("--in-url", help="search for results containing a specific content in URL")
    parser.add_argument("--in-title", help="search for results containing a specific title")
    parser.add_argument("--in-text", help="search for results containing a specific text")
    parser.add_argument("-n", "--num-pages", help="Number of pages to scrap from", default=1)
    parser.add_argument("-V", "--version", action="version", version="pysearch 1.0.0")
    parser.add_argument("-H", "--help-flags", action="store_true", help="show all available flags")
    args = parser.parse_args()
    intro = chalk.yellow('''
 /$$$$$$$                                                              /$$                          
| $$__  $$                                                            | $$                          
| $$  \ $$ /$$   /$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$                     
| $$$$$$$/| $$  | $$ /$$_____/ /$$__  $$ |____  $$ /$$__  $$ /$$_____/| $$__  $$                    
| $$____/ | $$  | $$|  $$$$$$ | $$$$$$$$  /$$$$$$$| $$  \__/| $$      | $$  \ $$                    
| $$      | $$  | $$ \____  $$| $$_____/ /$$__  $$| $$      | $$      | $$  | $$                    
| $$      |  $$$$$$$ /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$| $$  | $$                    
|__/       \____  $$|_______/  \_______/ \_______/|__/       \_______/|__/  |__/                    
           /$$  | $$                                                                                
          |  $$$$$$/                                                                                
           \______/                                                                                 
  /$$$$$$                                /$$                 /$$   /$$                     /$$      
 /$$__  $$                              | $$                | $$  | $$                    | $$      
| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$ | $$  /$$$$$$       | $$  | $$  /$$$$$$   /$$$$$$$| $$   /$$
| $$ /$$$$ /$$__  $$ /$$__  $$ /$$__  $$| $$ /$$__  $$      | $$$$$$$$ |____  $$ /$$_____/| $$  /$$/
| $$|_  $$| $$  \ $$| $$  \ $$| $$  \ $$| $$| $$$$$$$$      | $$__  $$  /$$$$$$$| $$      | $$$$$$/ 
| $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$| $$_____/      | $$  | $$ /$$__  $$| $$      | $$_  $$ 
|  $$$$$$/|  $$$$$$/|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$      | $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$
 \______/  \______/  \______/  \____  $$|__/ \_______/      |__/  |__/ \_______/ \_______/|__/  \__/
                               /$$  \ $$                                                            
                              |  $$$$$$/                                                            
                               \______/                                                             
 /$$    /$$   /$$        /$$$$$$      /$$$$$$                                                       
| $$   | $$ /$$$$       /$$$_  $$    /$$$_  $$                                                      
| $$   | $$|_  $$      | $$$$\ $$   | $$$$\ $$                                                      
|  $$ / $$/  | $$      | $$ $$ $$   | $$ $$ $$                                                      
 \  $$ $$/   | $$      | $$\ $$$$   | $$\ $$$$                                                      
  \  $$$/    | $$      | $$ \ $$$   | $$ \ $$$                                                      
   \  $/    /$$$$$$ /$$|  $$$$$$//$$|  $$$$$$/                                                      
    \_/    |______/|__/ \______/|__/ \______/                                                       
                                                                                                                                                                                                                                                                                                                                                                                     
    ''')

    # Check if the user requested help with the flags
    if args.help_flags:
        print(intro)
        print("\nUSAGE: pysearch [OPTIONS] QUERY\n")
        print("Search Google for QUERY.\n")
        print("OPTIONS:\n")
        print("-h, --help           Show this help message and exit.")
        print("-b, --brute-search   Perform a brute-force search.")
        print("-v, -verbose         Verbose mode.")
        print("-f, --filetype FILETYPE")
        print("                     Search for a specific file type.")
        print("-n, --num-pages      Select the number of pages to scrap from.")
        print("                     Default is 1.")
        print("-s, --site SITE      Search for results from a specific URL.")
        print("-d", "--delay        Delay between search requests.")
        print("                     Default is 5 s.")
        print("--in-url IN_URL      Search for results containing a specific URL.")
        print("--in-title IN_TITLE  Search for results containing a specific title.")
        print("--in-text IN_TEXT    Search for results containing a specific text.")
        print("-V, --version        Show program's version number and exit.\n")
        return 0

    # Print the program intro

    print(intro)
    print(chalk.bold("Credits:") + "                -       "+chalk.yellow.bold("A. Buschinelli (Anonymma)"))
    print(chalk.bold("GitHub") + "                  -       "+chalk.red.bold("http://github.com/buschinelli-joao"))
    print(chalk.bold("[*] ") + chalk.green.bold("Searching..."))
    results = googleScrapper(args.query, args.brute_search, args.filetype, args.site, args.in_url, args.in_title, args.num_pages, verbose=args.verbose, delay=args.delay)
    # Print the search results

    if results == []:
        print(chalk.red.bold("[!] ") + chalk.red("No results found for search. Consider changing delay between requests."))
    for item in results:
        print(chalk.bold("Title: ") + chalk.blue(item["title"]))
        print(chalk.bold("Link: ") + chalk.red(item['link']))
        print(chalk.bold("Snippet: ") + chalk.green(item["text"] + "\n"))

    

    return 0

if __name__ == '__main__':
    main()
