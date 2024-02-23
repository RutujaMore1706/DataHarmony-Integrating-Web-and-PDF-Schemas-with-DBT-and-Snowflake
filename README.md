## Assignment3

## How to run Application locally


To run the application locally from scratch, follow these steps:

1. **Clone the Repository**: Clone the repository onto your local machine.

   ```bash
   git clone https://github.com/BigDataIA-Spring2024-Sec1-Team4/Assignment3
   ```

2. **Create a Virtual Environment**: Set up a virtual environment to isolate project dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**: Activate the virtual environment.

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **Unix or MacOS**:

     ```bash
     source venv/bin/activate
     ```
     
4. **Host Grobid Server and Run Airflow**: Open Docker Desktop and host the Grobid server. (Run this in a separate terminal)

   ```bash
    docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.8.0
    docker-compose up -d
   ```