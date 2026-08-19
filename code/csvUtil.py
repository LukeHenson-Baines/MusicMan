try:
    import csv 
except ImportError:
    print("Please install reccommended dependency: csv.")
    quit()
    
# CSV Util
def load_csv(file_path):
    questions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        for row in csv_reader:
            questions.append((row[1], row[2]))
    return questions

# Function to create a CSV file and populate the first line
def create_csv_file(file_name, header):
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)