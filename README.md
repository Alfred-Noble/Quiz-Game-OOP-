# Quiz-Game-OOP-
Overview: The Quiz Game is an interactive Python application that leverages Object-Oriented Programming (OOP) principles to create an engaging and modular trivia experience. Designed to test and enhance your knowledge across various topics, this project showcases clean code architecture, efficient data management, and a user-friendly interface.

Features
1) Modular Design: The application is structured using multiple classes, each responsible for specific functionalities, ensuring scalability and maintainability.
2) Question Management: A dedicated class handles question fetching, parsing, and storing, supporting various formats (e.g., JSON, CSV) for flexibility.
3) Game Logic: The core game logic is encapsulated within a class that manages the flow of the quiz, score calculation, and user interactions.
4) User Interface: A separate class handles the user interface, providing a smooth and intuitive experience for players.
5) Randomization: Questions are randomized each game session to provide a unique experience every time.
6) Feedback System: Immediate feedback on answers to help players learn and improve their knowledge.

Classes
1) Quiz: Manages the overall game flow, including starting the quiz, processing answers, and keeping track of the score.
2) Question: Represents a quiz question, storing the question text, possible answers, and the correct answer.
3) QuestionBank: Responsible for loading and storing a collection of Question objects from various data sources.
