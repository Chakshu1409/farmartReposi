# Discussion.md

## Solutions Considered
1. Loading Entire File into Memory (Rejected: Not scalable for 1TB files)
2. Streaming Line-by-Line Processing (Accepted: Efficient memory usage)
3. Binary Search (if sorted logs) (Could be optimized further)

## Final Solution Summary
- We chose a streaming approach where we read the file line by line and extract logs matching the given date.
- This ensures minimal memory usage and good performance.

## Steps to Run
1. Clone the repository:  https://github.com/Chakshu1409/farmartReposi
2. Run the script:  python src/extract_logs.py YYYY-MM-DD
3. Output will be saved in `output/output_YYYY-MM-DD.txt`


