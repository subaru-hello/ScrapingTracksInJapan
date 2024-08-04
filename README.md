# ScrapingTracksInJapan
This repository is used to collect track data for use in the [TracksForPrivateAthleteDB](https://github.com/subaru-hello/TracksForPrivateAthleteDB) project.

### Objective
The objective of this project was to automate the collection of track availability data across various municipalities in Japan to maintain an up-to-date database for private athletes.

### Why
Many municipalities in Japan manage track availability through PDFs, making it cumbersome and time-consuming for private athletes to find and compile this information manually. Automating this process ensures that athletes have easy access to accurate and timely data, helping them plan their training schedules more effectively.

### How
To achieve this objective, I utilized Python for data collection. Here’s a step-by-step outline of the process:

1. **PDF Retrieval**: Identified numerous municipalities that manage track availability through publicly accessible PDFs on their websites.
2. **Automation with Python**: Wrote Python scripts to automate the downloading of these PDFs.
3. **Data Extraction**: Extracted relevant information from the PDFs and converted it into a structured CSV format.
4. **Documentation**: Documented the entire process to ensure reproducibility and ease of understanding.

For a detailed explanation of the methods used, please refer to the following articles:
- [Data Collection Method 1](https://zenn.dev/subaru_hello/articles/73253a46a76f7f)
- [Data Collection Method 2](https://zenn.dev/subaru_hello/articles/570e9e990374a6)
- [Data Collection Method 3](https://zenn.dev/subaru_hello/articles/38624760719abf)

This project not only streamlined the data collection process but also significantly reduced the time and effort required to maintain an accurate database for private athletes in Japan.
