*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Project: Operationalizing Machine Learning

First part of the project would involve training models using Azure AutoML with the Bank Marketing Dataset. Thereafter the best model will be deployed with an endpoint to be consumed using Swagger and Python requests. Next, using the same dataset, a AutoML pipeline will be created, published and consumed using Python requests. 

## Architectural Diagram
![image](https://user-images.githubusercontent.com/109334615/179765971-4b8db739-b0c4-4767-98ff-f7c6a7a6b489.png)

## Key Steps
1. Downloaded dataset is uploaded as bank-data. 
![data](https://user-images.githubusercontent.com/109334615/179766442-6da92603-7f58-4925-ba96-f2f2bf408039.PNG)

2. Completion of AutoML experiment
![automl-complete](https://user-images.githubusercontent.com/109334615/179766687-c03ed0c7-3857-4158-8a5b-9b097dc2aaaf.PNG)
![automl-complete2](https://user-images.githubusercontent.com/109334615/179766725-ccecfc04-82d2-45e7-82a2-a0cfe4ce35bb.PNG)

3. Best model generated from AutoML
![automl-bestmodel](https://user-images.githubusercontent.com/109334615/179766869-cd7f7033-3467-4d56-8e60-778943aa8b8f.PNG)

4. Application Insights is enabled
![application_insights_true](https://user-images.githubusercontent.com/109334615/179766986-ba184672-4faa-4d20-879a-5a7ba216182e.PNG)

5. Logs output from logs.py
![logs](https://user-images.githubusercontent.com/109334615/179767075-61266e79-f88f-404b-aba5-015a2027a0c2.PNG)

6. Consume endpoint using Swagger
![swagger](https://user-images.githubusercontent.com/109334615/179767172-ff5efe55-c0fd-4ab5-a29e-3be76a966483.PNG)
![swagger2](https://user-images.githubusercontent.com/109334615/179767183-2f058851-e8e0-4bf4-a14b-ffd5d2e1b635.PNG)

7. JSON output from model using endpoint.py
![endpoint_output](https://user-images.githubusercontent.com/109334615/179767328-ed931a2d-3808-49c8-95a9-4fa2d1e16437.PNG)

8. Benchmarking the model using Apache Benchmark
![benchmark](https://user-images.githubusercontent.com/109334615/179767495-b44675dc-d9f5-4ba0-937c-4394b9e96b19.PNG)

9. Creation of Pipeline in Azure ML studio
![pipeline_jobs](https://user-images.githubusercontent.com/109334615/179768243-0b7a5ee4-553e-420a-aaf7-f4677f56571c.PNG)

10. Creation of Pipeline Endpoints in Azure ML studio
![pipeline_endpoints](https://user-images.githubusercontent.com/109334615/179768387-80457ee9-edf0-418b-a792-7d51c3bbc4df.PNG)

11. Bankmarketing dataset uploaded in Azure ML studio
![bankmarketing_dataset](https://user-images.githubusercontent.com/109334615/179768509-6cfd26c4-9de3-449f-9187-df47497e3e5c.PNG)

12. Published endpoint overview of pipeline endpoint
![published_pipeline_overview](https://user-images.githubusercontent.com/109334615/179768607-8ab9c34a-57c8-4f33-b308-e013648a5598.PNG)

13. RunDetails Widget with step runs
![run_widget1](https://user-images.githubusercontent.com/109334615/179768735-7dde6920-f8ea-4694-8675-478d45a53973.PNG)
![run_widget2](https://user-images.githubusercontent.com/109334615/179768761-779e0bbf-6d08-42e1-b8e5-b1f0aaf48937.PNG)

14. Scheduled run
![scheduled_run_this](https://user-images.githubusercontent.com/109334615/179768834-f7a83511-cbbc-4837-b27e-4e7257b27dd1.PNG)

## Screen Recording
Screencast link: https://youtu.be/GMmWXOYv4PM
