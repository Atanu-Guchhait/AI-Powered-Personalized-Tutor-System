# AI-Powered-Personalized-Tutor-System


The AI-Powered Personal Tutor is an intelligent, scalable system designed to enhance student engagement by providing personalized learning experiences. Traditional educational methods often fail to address the diverse learning paces and styles of students. This project aims to leverage Artificial Intelligence to create a tutor that adapts to each student's unique needs, offering real-time feedback, customized learning paths, and interactive support. The goal is to provide students with a more engaging, effective, and personalized learning experience, making education more accessible and tailored.





Technology Used : 

Data Manipulation and Analysis: Numpy, Pandas for Pre-processing.

Data Visualization :  Matplotlib, Seaborn For visualization.

Machine Learning (ML): Scikit-learn, Pickle, Column Transformer, Scikit-learn Pipeline.

Natural Language Processing (NLP): For intelligent interaction with students, enabling them to ask questions and receive explanations in natural language.

Rag-Pipeline : For PDF Query.

Streamlit/HTML/CSS: For building interactive and user-friendly web interfaces for both students and educators.







System Architectural Flow : 

Flow of the Application:
Login/Registration Page: Users can register or log in.
Once logged in, users can access the  to navigate between the sections:
Student Promotion Prediction: Forecasting student readiness for the next level.
Assessment Score Prediction: Estimating future performance.
Level-Based Recommendations: Suggesting tailored materials for each student level.
Content Retention/Skipping: Identifying essential content and what can be skipped.
PDF Querying: Extracting insights from uploaded PDFs.


Result : 
Student Promotion Prediction
Model: RandomForestClassifier
Metrics: Accuracy Score, Confusion Matrix
Results: 99.99% accuracy score, ensuring high-quality recommendations.

Content Recommendation
Model: Softmax Regression 
Metrics: Accuracy Score, Confusion Matrix
Results: 100% accurate in Content Recommendation.

Assesment Score Prediction
Model: RandomForestRegressor
Metrics: Mean squared error, r2score
Results: MSE : 0.0008, r2score : 100%

Content Retention/Skipping
Model: xgbClassifier
Metrics: Accuracy Score, Confusion Matrix
Results:  100% Accuracy score



Challenges and Limitations:
Data Quality & Availability
Inconsistent or insufficient data can affect recommendation accuracy. Requires large, high-quality datasets for effective learning.
Computational Requirements
High processing power needed for AI models, especially NLP-based components. Real-time response optimization for smooth user experience.
Integration with External Platforms
Difficulty in integrating with job portals, course providers, and learning platforms. API limitations and changing platform policies.
PDF Query accuracy : 
Ensuring generated answer are meaningful and not overly simple or complex.
May require human validation for high-stakes assessments.


Conclusion:
The AI-Powered Personal Tutor effectively enhances learning through personalized recommendations, PDF Query, Student Promotion and Assesment Score Prediction,. Despite challenges like data quality, model bias, and computational requirements, the system demonstrates high accuracy, engagement, and scalability. Future improvements will focus on refining AI models, ensuring fairness, and enhancing user experience to create a truly adaptive learning platform.

Video : 
https://github.com/user-attachments/assets/b65417ad-6a87-4e08-b19b-016cfc14d5c3

