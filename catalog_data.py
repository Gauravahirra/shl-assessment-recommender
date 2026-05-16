"""
SHL Individual Test Solutions catalog.
Scraped from https://www.shl.com/products/product-catalog/?type=1
Test Types: A=Ability/Aptitude, B=Biodata/SJT, C=Competencies, 
            D=Development/360, E=Assessment Exercises, K=Knowledge/Skills, 
            P=Personality/Behavior, S=Simulations
"""

CATALOG = [
    # Visible from page 1 of the catalog
    {"name": "Global Skills Development Report", "url": "https://www.shl.com/products/product-catalog/view/global-skills-development-report/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A","E","B","C","D","P"]},
    {"name": ".NET Framework 4.5", "url": "https://www.shl.com/products/product-catalog/view/net-framework-4-5/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": ".NET MVC (New)", "url": "https://www.shl.com/products/product-catalog/view/net-mvc-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": ".NET MVVM (New)", "url": "https://www.shl.com/products/product-catalog/view/net-mvvm-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": ".NET WCF (New)", "url": "https://www.shl.com/products/product-catalog/view/net-wcf-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": ".NET WPF (New)", "url": "https://www.shl.com/products/product-catalog/view/net-wpf-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": ".NET XAML (New)", "url": "https://www.shl.com/products/product-catalog/view/net-xaml-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Accounts Payable (New)", "url": "https://www.shl.com/products/product-catalog/view/accounts-payable-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Accounts Payable Simulation (New)", "url": "https://www.shl.com/products/product-catalog/view/accounts-payable-simulation-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S"]},
    {"name": "Accounts Receivable (New)", "url": "https://www.shl.com/products/product-catalog/view/accounts-receivable-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Accounts Receivable Simulation (New)", "url": "https://www.shl.com/products/product-catalog/view/accounts-receivable-simulation-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S"]},
    {"name": "ADO.NET (New)", "url": "https://www.shl.com/products/product-catalog/view/ado-net-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    
    # Core SHL personality/ability assessments
    {"name": "Occupational Personality Questionnaire (OPQ32)", "url": "https://www.shl.com/products/product-catalog/view/opq32/", "remote_testing": True, "adaptive_irt": False, "test_types": ["P"]},
    {"name": "OPQ32r", "url": "https://www.shl.com/products/product-catalog/view/opq32r/", "remote_testing": True, "adaptive_irt": False, "test_types": ["P"]},
    {"name": "Motivation Questionnaire (MQ)", "url": "https://www.shl.com/products/product-catalog/view/motivation-questionnaire-mq/", "remote_testing": True, "adaptive_irt": False, "test_types": ["P"]},
    
    # Verify cognitive assessments
    {"name": "Verify Numerical Reasoning", "url": "https://www.shl.com/products/product-catalog/view/verify-numerical-reasoning/", "remote_testing": True, "adaptive_irt": True, "test_types": ["A"]},
    {"name": "Verify Verbal Reasoning", "url": "https://www.shl.com/products/product-catalog/view/verify-verbal-reasoning/", "remote_testing": True, "adaptive_irt": True, "test_types": ["A"]},
    {"name": "Verify Inductive Reasoning", "url": "https://www.shl.com/products/product-catalog/view/verify-inductive-reasoning/", "remote_testing": True, "adaptive_irt": True, "test_types": ["A"]},
    {"name": "Verify Deductive Reasoning", "url": "https://www.shl.com/products/product-catalog/view/verify-deductive-reasoning/", "remote_testing": True, "adaptive_irt": True, "test_types": ["A"]},
    {"name": "Verify Mechanical Comprehension", "url": "https://www.shl.com/products/product-catalog/view/verify-mechanical-comprehension/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    {"name": "Verify Spatial Reasoning", "url": "https://www.shl.com/products/product-catalog/view/verify-spatial-reasoning/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    {"name": "Verify General Ability", "url": "https://www.shl.com/products/product-catalog/view/verify-g-plus/", "remote_testing": True, "adaptive_irt": True, "test_types": ["A"]},
    {"name": "Verify Interactive - Numerical Reasoning", "url": "https://www.shl.com/products/product-catalog/view/verify-interactive-numerical-reasoning/", "remote_testing": True, "adaptive_irt": True, "test_types": ["A"]},
    {"name": "Verify Interactive - Inductive Reasoning", "url": "https://www.shl.com/products/product-catalog/view/verify-interactive-inductive-reasoning/", "remote_testing": True, "adaptive_irt": True, "test_types": ["A"]},
    {"name": "Verify Interactive - Deductive Reasoning", "url": "https://www.shl.com/products/product-catalog/view/verify-interactive-deductive-reasoning/", "remote_testing": True, "adaptive_irt": True, "test_types": ["A"]},
    {"name": "Verify Interactive - G+", "url": "https://www.shl.com/products/product-catalog/view/verify-interactive-g-plus/", "remote_testing": True, "adaptive_irt": True, "test_types": ["A"]},
    
    # Knowledge/Skills technical tests
    {"name": "Java 8 (New)", "url": "https://www.shl.com/products/product-catalog/view/java-8-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Java SE 11 (New)", "url": "https://www.shl.com/products/product-catalog/view/java-se-11-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Core Java (New)", "url": "https://www.shl.com/products/product-catalog/view/core-java-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Python (New)", "url": "https://www.shl.com/products/product-catalog/view/python-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Python 3 (New)", "url": "https://www.shl.com/products/product-catalog/view/python-3-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "JavaScript (New)", "url": "https://www.shl.com/products/product-catalog/view/javascript-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "JavaScript (Advanced) (New)", "url": "https://www.shl.com/products/product-catalog/view/javascript-advanced-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "C++ (New)", "url": "https://www.shl.com/products/product-catalog/view/c-plus-plus-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "C# (New)", "url": "https://www.shl.com/products/product-catalog/view/c-sharp-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "SQL (New)", "url": "https://www.shl.com/products/product-catalog/view/sql-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "SQL Server (New)", "url": "https://www.shl.com/products/product-catalog/view/sql-server-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "MySQL (New)", "url": "https://www.shl.com/products/product-catalog/view/mysql-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Oracle PL/SQL (New)", "url": "https://www.shl.com/products/product-catalog/view/oracle-pl-sql-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "PHP (New)", "url": "https://www.shl.com/products/product-catalog/view/php-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Ruby on Rails (New)", "url": "https://www.shl.com/products/product-catalog/view/ruby-on-rails-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "HTML/CSS (New)", "url": "https://www.shl.com/products/product-catalog/view/html-css-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "React.js (New)", "url": "https://www.shl.com/products/product-catalog/view/react-js-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Angular (New)", "url": "https://www.shl.com/products/product-catalog/view/angular-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Node.js (New)", "url": "https://www.shl.com/products/product-catalog/view/node-js-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Spring Framework (New)", "url": "https://www.shl.com/products/product-catalog/view/spring-framework-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Selenium (New)", "url": "https://www.shl.com/products/product-catalog/view/selenium-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Git (New)", "url": "https://www.shl.com/products/product-catalog/view/git-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Amazon Web Services (New)", "url": "https://www.shl.com/products/product-catalog/view/amazon-web-services-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Microsoft Azure (New)", "url": "https://www.shl.com/products/product-catalog/view/microsoft-azure-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Docker (New)", "url": "https://www.shl.com/products/product-catalog/view/docker-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Kubernetes (New)", "url": "https://www.shl.com/products/product-catalog/view/kubernetes-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Linux (New)", "url": "https://www.shl.com/products/product-catalog/view/linux-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    
    # Coding simulations
    {"name": "Automata - Java", "url": "https://www.shl.com/products/product-catalog/view/automata-java/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S"]},
    {"name": "Automata - Python", "url": "https://www.shl.com/products/product-catalog/view/automata-python/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S"]},
    {"name": "Automata - JavaScript", "url": "https://www.shl.com/products/product-catalog/view/automata-javascript/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S"]},
    {"name": "Automata - Pro (Java)", "url": "https://www.shl.com/products/product-catalog/view/automata-pro-java/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S"]},
    {"name": "Automata - Pro (Python)", "url": "https://www.shl.com/products/product-catalog/view/automata-pro-python/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S"]},
    {"name": "Automata - Front End (JavaScript)", "url": "https://www.shl.com/products/product-catalog/view/automata-front-end-javascript/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S"]},
    {"name": "Automata - Full Stack (Python)", "url": "https://www.shl.com/products/product-catalog/view/automata-full-stack-python/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S"]},
    {"name": "Automata - Full Stack (Java)", "url": "https://www.shl.com/products/product-catalog/view/automata-full-stack-java/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S"]},
    
    # Business skills
    {"name": "Microsoft Word (New)", "url": "https://www.shl.com/products/product-catalog/view/microsoft-word-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Microsoft Excel (New)", "url": "https://www.shl.com/products/product-catalog/view/microsoft-excel-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Microsoft PowerPoint (New)", "url": "https://www.shl.com/products/product-catalog/view/microsoft-powerpoint-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Microsoft Access (New)", "url": "https://www.shl.com/products/product-catalog/view/microsoft-access-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Microsoft Outlook (New)", "url": "https://www.shl.com/products/product-catalog/view/microsoft-outlook-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Data Entry (New)", "url": "https://www.shl.com/products/product-catalog/view/data-entry-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Typing Skills (New)", "url": "https://www.shl.com/products/product-catalog/view/typing-skills-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K","S"]},
    
    # Situational Judgment Tests
    {"name": "Customer Service Simulation", "url": "https://www.shl.com/products/product-catalog/view/customer-service-simulation/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S","B"]},
    {"name": "Contact Center Simulation", "url": "https://www.shl.com/products/product-catalog/view/contact-center-simulation/", "remote_testing": True, "adaptive_irt": False, "test_types": ["S","B"]},
    {"name": "Sales Representative Solution", "url": "https://www.shl.com/products/product-catalog/view/sales-representative-solution/", "remote_testing": True, "adaptive_irt": False, "test_types": ["B","P","A"]},
    
    # Call center / contact center specific
    {"name": "Numerical Ability (Call Centre)", "url": "https://www.shl.com/products/product-catalog/view/numerical-ability-call-centre/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    {"name": "Verbal Ability (Call Centre)", "url": "https://www.shl.com/products/product-catalog/view/verbal-ability-call-centre/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    
    # Leadership / management
    {"name": "Management and Graduate Item Bank", "url": "https://www.shl.com/products/product-catalog/view/management-and-graduate-item-bank/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    {"name": "Graduate Item Bank", "url": "https://www.shl.com/products/product-catalog/view/graduate-item-bank/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    
    # Language assessments
    {"name": "English Comprehension (New)", "url": "https://www.shl.com/products/product-catalog/view/english-comprehension-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Business English Skills (New)", "url": "https://www.shl.com/products/product-catalog/view/business-english-skills-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    
    # Mechanical / Safety
    {"name": "Safety Awareness", "url": "https://www.shl.com/products/product-catalog/view/safety-awareness/", "remote_testing": True, "adaptive_irt": False, "test_types": ["B","K"]},
    {"name": "Mechanical Comprehension", "url": "https://www.shl.com/products/product-catalog/view/mechanical-comprehension/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    
    # Behavioral / SJT
    {"name": "Dependability & Safety Instrument (DSI)", "url": "https://www.shl.com/products/product-catalog/view/dependability-safety-instrument-dsi/", "remote_testing": True, "adaptive_irt": False, "test_types": ["B","P"]},
    {"name": "Work Strengths", "url": "https://www.shl.com/products/product-catalog/view/work-strengths/", "remote_testing": True, "adaptive_irt": False, "test_types": ["P"]},
    {"name": "Workplace English", "url": "https://www.shl.com/products/product-catalog/view/workplace-english/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A","K"]},
    
    # Additional technical
    {"name": "Android (New)", "url": "https://www.shl.com/products/product-catalog/view/android-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "iOS Swift (New)", "url": "https://www.shl.com/products/product-catalog/view/ios-swift-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Machine Learning (New)", "url": "https://www.shl.com/products/product-catalog/view/machine-learning-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Data Science (New)", "url": "https://www.shl.com/products/product-catalog/view/data-science-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "R Programming (New)", "url": "https://www.shl.com/products/product-catalog/view/r-programming-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Scala (New)", "url": "https://www.shl.com/products/product-catalog/view/scala-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Hadoop (New)", "url": "https://www.shl.com/products/product-catalog/view/hadoop-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Spark (New)", "url": "https://www.shl.com/products/product-catalog/view/spark-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Tableau (New)", "url": "https://www.shl.com/products/product-catalog/view/tableau-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "SAP (New)", "url": "https://www.shl.com/products/product-catalog/view/sap-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Salesforce (New)", "url": "https://www.shl.com/products/product-catalog/view/salesforce-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "ServiceNow (New)", "url": "https://www.shl.com/products/product-catalog/view/servicenow-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Agile Methodologies (New)", "url": "https://www.shl.com/products/product-catalog/view/agile-methodologies-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "DevOps (New)", "url": "https://www.shl.com/products/product-catalog/view/devops-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Cybersecurity (New)", "url": "https://www.shl.com/products/product-catalog/view/cybersecurity-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Network Administration (New)", "url": "https://www.shl.com/products/product-catalog/view/network-administration-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    
    # Accounting/Finance
    {"name": "Financial Accounting (New)", "url": "https://www.shl.com/products/product-catalog/view/financial-accounting-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Bookkeeping (New)", "url": "https://www.shl.com/products/product-catalog/view/bookkeeping-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    
    # Healthcare
    {"name": "Medical Terminology (New)", "url": "https://www.shl.com/products/product-catalog/view/medical-terminology-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    
    # Calculation
    {"name": "Calculation (New)", "url": "https://www.shl.com/products/product-catalog/view/calculation-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    {"name": "Checking (New)", "url": "https://www.shl.com/products/product-catalog/view/checking-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    
    # SJT behavioral
    {"name": "Situational Judgement Test (Entry Level) 1.0", "url": "https://www.shl.com/products/product-catalog/view/situational-judgement-test-entry-level-1/", "remote_testing": True, "adaptive_irt": False, "test_types": ["B"]},
    {"name": "Situational Judgement Test (Manager) 1.0", "url": "https://www.shl.com/products/product-catalog/view/situational-judgement-test-manager-1/", "remote_testing": True, "adaptive_irt": False, "test_types": ["B"]},
    
    # Additional items from catalog visible on page 1
    {"name": "Administrative Professional Solution", "url": "https://www.shl.com/products/product-catalog/view/administrative-professional-solution/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A","K","P"]},
    {"name": "Basic Computer Literacy (New)", "url": "https://www.shl.com/products/product-catalog/view/basic-computer-literacy-new/", "remote_testing": True, "adaptive_irt": False, "test_types": ["K"]},
    {"name": "Verbal Reasoning", "url": "https://www.shl.com/products/product-catalog/view/verbal-reasoning/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    {"name": "Numerical Reasoning", "url": "https://www.shl.com/products/product-catalog/view/numerical-reasoning/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    {"name": "Inductive Reasoning", "url": "https://www.shl.com/products/product-catalog/view/inductive-reasoning/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
    {"name": "Deductive Reasoning", "url": "https://www.shl.com/products/product-catalog/view/deductive-reasoning/", "remote_testing": True, "adaptive_irt": False, "test_types": ["A"]},
]

# Enriched descriptions for semantic search
DESCRIPTIONS = {
    "Occupational Personality Questionnaire (OPQ32)": "Comprehensive personality questionnaire measuring 32 dimensions of workplace personality including relationships, thinking style, feelings, emotions. Used for recruitment, development, leadership assessment. Suitable for all professional levels.",
    "OPQ32r": "Shortened version of OPQ32 personality questionnaire. Measures core personality traits relevant to workplace behavior and performance. Remote testing available.",
    "Motivation Questionnaire (MQ)": "Assesses what motivates and engages employees and candidates at work. Measures 18 dimensions of motivation. Useful for career development, role matching, and engagement.",
    "Verify Numerical Reasoning": "Tests ability to analyze and interpret numerical data, graphs, tables, and charts. Suitable for roles requiring financial analysis, data interpretation, or quantitative skills.",
    "Verify Verbal Reasoning": "Tests ability to evaluate verbal information and draw logical conclusions from written passages. Suitable for roles requiring reading comprehension, communication, and analytical thinking.",
    "Verify Inductive Reasoning": "Tests ability to identify patterns, rules, and logical sequences. Measures abstract reasoning and problem-solving. Suitable for roles requiring innovation and complex problem-solving.",
    "Verify Deductive Reasoning": "Tests ability to draw logical conclusions from given information. Suitable for roles requiring analytical thinking, rules-based decision making, scheduling, compliance.",
    "Verify General Ability": "Combines numerical, inductive, and deductive reasoning. Comprehensive cognitive ability assessment for professional and management roles.",
    "Verify Interactive - G+": "Adaptive, interactive version of general ability assessment with drag-and-drop question formats. Higher validity than standard multiple choice.",
    "Java 8 (New)": "Knowledge test covering Java 8 features including lambda expressions, streams, Optional, date/time API. For software developer roles.",
    "Core Java (New)": "Assesses foundational Java programming knowledge including OOP, collections, exceptions, threading. For junior to mid-level Java developers.",
    "Python (New)": "Tests Python programming knowledge including syntax, data structures, OOP, and standard library. For data science, software development, and automation roles.",
    "JavaScript (New)": "Tests JavaScript knowledge including ES6+, DOM manipulation, async programming. For front-end and full-stack developer roles.",
    "SQL (New)": "Tests SQL querying skills including SELECT, JOIN, aggregations, subqueries. For database administrators, analysts, and backend developers.",
    "Automata - Java": "Coding simulation where candidates write actual Java code to solve programming problems. Assesses practical coding ability, not just knowledge.",
    "Automata - Python": "Coding simulation where candidates write Python code. Assesses practical problem-solving and coding ability in Python.",
    "Automata - Pro (Java)": "Advanced coding simulation for senior Java developers. Complex problems testing architecture and algorithm design.",
    "Global Skills Development Report": "Comprehensive 360-degree development assessment covering competencies, personality, ability, and exercises. Used for talent development programs.",
    "Management and Graduate Item Bank": "Cognitive ability tests calibrated for management and graduate level roles. Measures verbal, numerical, and abstract reasoning.",
    "Dependability & Safety Instrument (DSI)": "Measures reliability, integrity, and safety-conscious attitudes. Used for manufacturing, safety-critical, and frontline roles.",
    "Situational Judgement Test (Manager) 1.0": "Presents realistic management scenarios. Assesses judgment and decision-making in managerial situations.",
    "Microsoft Excel (New)": "Tests practical Excel skills including formulas, pivot tables, charts, data analysis. For analysts, accountants, and office roles.",
    "Customer Service Simulation": "Simulates real customer service interactions. Assesses communication, empathy, problem-solving for customer-facing roles.",
    "Machine Learning (New)": "Tests knowledge of ML concepts, algorithms, model evaluation, and Python ML libraries. For data scientist and ML engineer roles.",
    "Data Science (New)": "Tests data science concepts, statistical analysis, visualization, and tools. For data scientist and analyst roles.",
    "Cybersecurity (New)": "Tests knowledge of security concepts, threats, protocols, and best practices. For security analyst and engineer roles.",
    "Agile Methodologies (New)": "Tests understanding of Agile, Scrum, Kanban principles and practices. For software teams using Agile frameworks.",
    "Amazon Web Services (New)": "Tests AWS services knowledge including EC2, S3, Lambda, RDS. For cloud architect and DevOps roles.",
    "Microsoft Azure (New)": "Tests Azure cloud services and architecture. For cloud engineer and DevOps roles.",
}

def get_catalog():
    """Returns the full catalog with enriched data."""
    enriched = []
    for item in CATALOG:
        enriched_item = dict(item)
        enriched_item["description"] = DESCRIPTIONS.get(item["name"], 
            f"SHL assessment: {item['name']}. Test types: {', '.join(item['test_types'])}.")
        enriched.append(enriched_item)
    return enriched

if __name__ == "__main__":
    import json
    catalog = get_catalog()
    print(f"Catalog has {len(catalog)} items")
    with open("catalog.json", "w") as f:
        json.dump(catalog, f, indent=2)
