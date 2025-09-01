# F1 Driver Performance Analysis

## About The Project

[![F1 Driver Analysis][Demo-screenshot]](https://ddedida-f1-driver-analysis.streamlit.app/)

This project is a learning exercise focused on building a data pipeline for Formula 1 data. The data is sourced from Kaggle in csv format, loaded into PostgreSQL, then stored in Snowflake, and finally visualized through several analyses using Streamlit.

Dataset Link: [Formula 1 Dataset](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020/)
<br>
Demo Link: https://ddedida-f1-driver-analysis.streamlit.app/

### Data Pipeline Architecture

![Data Pipeline Flow][Data-pipeline-flow]

### Built With

- [![Python][Python-badge]][Python-url]
- [![PostgreSQL][PostgreSQL-badge]][PostgreSQL-url]
- [![Snowflake][Snowflake-badge]][Snowflake-url]
- [![Streamlit][Streamlit-badge]][Streamlit-url]

<!-- GETTING STARTED -->

## Getting Started

These are the steps of how to run the project on your local

### Prerequisite

- [Python 3.9+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Snowflake Account](https://signup.snowflake.com/)
- [VS Code](https://code.visualstudio.com/) or any preferred IDE

### Set Up the Project

1. Clone the repo
   ```sh
   git clone https://github.com/ddedida/f1-driver-analysis.git
   ```
2. Make your own pyton virtual environment
   ```sh
   python -m venv venv
   ```
3. Activate venv
   ```sh
   .\venv\Scripts\activate
   ```
4. (Optional) upgrade pip first
   ```sh
   pip install --upgrade pip
   ```
5. Install all the depedencies on requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
6. Copy `.env.example` file and rename it to `.env`
7. Change all existing values according to your settings

   ```sh
   HOST=localhost
   PORT=5432
   DBNAME=example_db
   USER=example_user
   PASSWORD=example_password

   SNOWFLAKE_USER=example_sf_user
   SNOWFLAKE_PASSWORD=example_sf_password
   SNOWFLAKE_ACCOUNT=example_sf_account
   SNOWFLAKE_WAREHOUSE=example_sf_warehouse
   SNOWFLAKE_DATABASE=example_sf_database
   SNOWFLAKE_SCHEMA=example_sf_schema
   SNOWFLAKE_ROLE=example_sf_role
   ```

<i>💡 If you want to skip the setup and go straight to the visualization, see the Run Streamlit section <a href="#streamlit">below</a>.</i>

### Load Data from CSV File to PostgreSQL

8. Open postgresql or pgadmin and run `create-table-postgre.sql` query from `etl\sql-query` folder
9. Go to the etl folder
   ```sh
   cd etl
   ```
10. Open VS Code command palette by pressing `ctrl+shift+p`
11. Search python interpreter and select `venv` (usually has a recommendation label)
12. Run file
    ```sh
    python .\csv_to_postgres.py
    ```

### Store Data to Snowflake

13. After loading the data into PostgreSQL, store it in Snowflake by running the `postgres_to_snowflake_raw.py` file:
    ```sh
    python .\postgres_to_snowflake_raw.py
    ```
14. Since some columns have incorrect data types, the data needs to be transformed from the `raw` schema to the `analytics` schema. Create a worksheet in Snowflake and run the `transform-raw-to-analytics-snowflake.sql` query.

### Create Views for Analytics

15. Currently, there are 3 analysis visualizations. Therefore, 3 corresponding views are provided. You can run the following SQL files in Snowflake worksheet:
    - `driver-average-pace.sql`
    - `driver-teammate-comparison.sql`
    - `driver-lap-time.sql`
16. Download the CSV files generated from these views and save them in the `data` folder.

<a id="streamlit"></a>

### Run Streamlit

17. Go to the `dashboard` folder
    ```sh
    cd dashboard
    ```
18. Run `main.py` file
    ```sh
    streamlit run .\main.py
    ```
19. All set! 🥳🎉

<!-- FUTURE UPDATE -->

## Future Update

- [ ] Add apache airflow in one of the processes

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<!-- CONTACT -->

## Contact

Dewangga Dika Darmawan - [@dewangga3d](https://www.instagram.com/dewangga3d/) - dewangga3d@gmail.com
Project Link: [f1-driver-analysis](https://github.com/ddedida/f1-driver-analysis)

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Formula 1 Dataset by rohanrao](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020/data)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [Readme Template by othneildrew](https://github.com/othneildrew/Best-README-Template/tree/main)

<!-- MARKDOWN LINKS & IMAGES -->

[Data-pipeline-flow]: image/data-pipeline-flow.png
[Demo-screenshot]: image/demo-screenshot.png
[Python-badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[PostgreSQL-badge]: https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
[Snowflake-badge]: https://img.shields.io/badge/Snowflake-29B5E8?logo=snowflake&logoColor=fff&style=for-the-badge
[Snowflake-url]: https://www.snowflake.com/en/
[Streamlit-badge]: https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=for-the-badge
[Streamlit-url]: https://streamlit.io/
