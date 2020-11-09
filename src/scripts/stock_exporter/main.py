import config as config
import force_format as formatter
import stock_html as sh

def main():
  # Logs into the website and retrieves the stock information
  stock = sh.stock_access(config.login_info)

  # uses beautiful soup to parse html document for text and exports it to a file
  sh.parse_data(stock)

  # cuts and formats the data returning a .csv file
  formatter.format()
  
main()

