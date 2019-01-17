import config
import export

def format():
  # open text documents we will be reading and writing to.
  data = open(config.parsed_name, "r")
  export_data = open(config.doc_name, "w") 
  export_file = config.doc_name

  # call the export function
  export.export(export_file)
  
  # take in line content of the text document
  # searchlines is an array of strings
  searchlines = data.readlines()

  counter = 0

  # if the line is between start and end line conditions print it and a comma
  for line in searchlines:
    if line != "\n":
      counter = counter + 1
      info = line.replace(" ",",").rstrip()
      comma_value = info + ','
      if counter >= config.start_condition and counter < config.end_condition:
        print(comma_value)

  export_data.close()
  data.close()
