import sys
import os

def extract_logs(log_file, target_date):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        with open(log_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                if line.startswith(target_date):
                    outfile.write(line)
        
        print(f"Logs for {target_date} have been saved to {output_file}")

    except FileNotFoundError:
        print("Log file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/extract_logs.py YYYY-MM-DD")
        sys.exit(1)
    
    log_file_path = "test_logs.log"  # Update with actual file path
    date_argument = sys.argv[1]

    extract_logs(log_file_path, date_argument)
