### ChurnGuard Project

**Minh Tran**

#### Executive summary
This report provides a comprehensive analysis of predictive analytics for customer retention in Bank X's mobile banking application. The study focuses on three key models—Logistic Regression, Random Forest, and Gradient Boosting—evaluating their performance metrics and feature importance in predicting customer churn. The findings offer valuable insights to proactively identify and mitigate factors contributing to churn, laying the foundation for strategic customer retention initiatives.

**Model Performance Overview:**
- All models demonstrate high accuracy, with Random Forest and Gradient Boosting consistently outperforming Logistic Regression.
- Minimal overfitting is observed, indicating robust generalization to unseen data.
- Fine-tuned specifications enhance model performance, with Random Forest and Gradient Boosting achieving accuracy rates of 94% and 95%, respectively.

**Feature Importance Insights:**
- User engagement emerges as a critical factor, with the frequency of logins within the last month (LOGIN_MB2_DAY_CNT_1M) identified as the most significant predictor of churn.
- Credit card management activities, financial transactions, and diverse app usage patterns also play pivotal roles in predicting and mitigating customer churn.
- Factors such as age, security awareness, and organic channel adoption contribute to the overall predictive power of the models.

**Strategic Recommendations:**
1. **User Engagement Campaigns:** Initiate targeted campaigns to enhance user engagement, leveraging insights from the most critical feature—frequency of logins within the last month.
  
2. **Credit Card Management Support:** Provide personalized support and promotions to users engaging in credit card management activities, fostering loyalty and continued credit card usage.

3. **Enhanced App Features:** Focus on improving and promoting features related to account information, transactions, and top-up activities to ensure a seamless user experience.

4. **Financial Education and Assistance:** Implement educational campaigns and financial assistance programs to encourage increased financial activities, including credit transactions.

5. **Targeted Marketing for E-commerce Users:** Launch campaigns specifically tailored to users with significant spending on E-commerce transactions from credit card accounts.

The predictive analytics framework presented in this report provides Bank X with actionable insights to proactively address customer churn in its mobile application. By implementing the recommended strategies and continuously refining the predictive models, Bank X is poised to enhance customer retention, strengthen user engagement, and ultimately elevate the overall customer experience.


#### Rationale
Customer churn in Bank X's mobile application is a critical concern that warrants careful examination and strategic intervention. This issue extends beyond mere numerical losses and financial implications; it strikes at the core of the bank's reputation, customer trust, and the sustainability of its digital ecosystem.

Firstly, in the context of financial repercussions, customer churn poses a direct threat to Bank X's revenue streams. The acquisition cost of each customer is a substantial investment, and losing customers prematurely undermines the return on this investment. By understanding and mitigating churn, Bank X can safeguard its financial stability and ensure the optimal utilization of resources.

Secondly, the digital landscape is fiercely competitive, with users having an array of alternatives at their fingertips. Customer churn not only results in a numerical loss but also opens the door for competitors to capitalize on disenchanted users. Preserving and expanding the customer base is not just a matter of financial prudence; it is a strategic imperative to maintain Bank X's competitive edge in the digital banking arena.

Furthermore, the intangible yet invaluable elements of trust and brand loyalty are at stake. Customers who abandon the mobile application may carry negative sentiments, impacting the bank's reputation. In the era of social media and instant communication, a dissatisfied customer has the potential to influence a network of peers, compounding the impact of churn on Bank X's brand equity.

In essence, caring about customer churn in Bank X's app is not merely a matter of statistical concern but a strategic imperative that encompasses financial stability, competitive resilience, and the preservation of the bank's intangible assets—customer trust and brand reputation. It is through a nuanced understanding of these interconnected facets that Bank X can institute effective measures to predict, prevent, and mitigate the challenges posed by customer churn in its mobile application.


#### Research Question
How can predictive analytics be leveraged to proactively identify and mitigate factors contributing to customer churn in mobile application of bank X?

#### Data Sources
The desired dataset for the research on predicting and mitigating customer churn in bank X's mobile application should be comprehensive, diverse, and representative of the bank's customer base. The dataset should encompass a range of variables that capture various aspects of user behavior, transactional activities, and engagement with the mobile application. 

Following are key characteristics of the desired dataset:
- **User Demographics**: Personal information such as age, gender, location, and occupation to understand the diverse user base.
- **Transactional Data**: 
	- Details of individual transactions, including frequency, types, and amounts.
	- Historical transactional patterns to identify trends and anomalies.
- **App Usage Metrics**:
	- Frequency and duration of app usage to gauge user engagement.
	- Specific features or services within the app that users interact with the most.
- **Churn Indicator**:
	- Binary indicator (1 or 0) representing whether a customer has churned or not.
	- Clearly defined criteria for categorizing a user as churned.
- **External Factors**: External variables that may influence customer behavior, such as economic indicators, industry trends, or competitive offerings.

By incorporating these characteristics, the desired dataset will serve as a robust foundation for conducting a thorough analysis of customer churn in bank X’s mobile application, enabling the development of accurate and actionable predictive models.

The data would be collected from internal source of bank X and external environment where bank X is operating.

The actual data obtained is as follows.

|Feature dimensions|Metrics                  	 	|Description                                                                                                             			   |
|------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|Churn indicator   |CHURN_FLAG               	 	|Customer not log in app in previous month                                                                               			   |
|Demographic       |AGE                      	 	|Customer age                                                                                                            			   |
|                  |GENDER                   	 	|Gender                                                                                                                  			   |
|App Usage Metrics |VIEW_ACCOUNT_INFO_CNT_3M 	 	|Frequency that customer view account information in app                                                                 			   |
|                  |ACCOUNT_MANAGEMENT_CNT_3M	 	|Frequency that customer view account management in app                                                                  			   |
|                  |LOAN_MANAGEMENT_CNT_3M   	 	|Frequency that customer view loan management in app                                                                     			   |
|                  |CREDIT_CARD_MANAGEMENT_CNT_3M	|Frequency that customer view credit card management in app                                                              			   |
|                  |MORE_USAGE_CNT_3M       	 	|Frequency that customer view other than account information, account information, loan management, credit card management in app		   |
|                  |SECURITY_CNT_3M         	 	|Frequency that customer view security functions in app                                                                  			   |
|                  |AR_CNT_3M               	 	|Frequency that customer view AR functions in app                                                                        			   |
|                  |PIGGY_CNT_3M            	 	|Frequency that customer view Piggy Campaign functions in app                                                            			   |
|                  |VOICEBOT_CNT_3M         	 	|Frequency that customer view Voicebot functions in app                                                                  			   |
|                  |VIB_CARE_INSURANCE_CNT_3M	 	|Frequency that customer purchase successfully insurance in app                                                          			   |
|                  |VIEW_ACCOUNT_INFO_DAY_CNT_3M 	|Number of distinct days that customer view account information in app                                                   			   |
|                  |ACCOUNT_MANAGEMENT_DAY_CNT_3M	|Number of distinct days that customer view account management in app                                                    			   |
|                  |LOAN_MANAGEMENT_DAY_CNT_3M	 	|Number of distinct days that customer view loan management in app                                                       			   |
|                  |CREDIT_CARD_MANAGEMENT_DAY_CNT_3M	|Number of distinct days that customer view credit card management in app                                                			   |
|                  |MORE_USAGE_DAY_CNT_3M   		|Number of distinct days that customer view other than account information, account information, loan management, credit card management in app	   |
|                  |SECURITY_DAY_CNT_3M     		|Number of distinct days that customer view security functions in app                                                    			   |
|                  |AR_DAY_CNT_3M           		|Number of distinct days that customer view AR functions in app                                                          			   |
|                  |PIGGY_DAY_CNT_3M        		|Number of distinct days that customer view Piggy Campaign functions in app                                              			   |
|                  |VOICEBOT_DAY_CNT_3M     		|Number of distinct days that customer view Voicebot functions in app                                                    			   |
|                  |VIB_CARE_INSURANCE_DAY_CNT_3M	|Number of distinct days that customer purchase successfully insurance in app                                            			   |
|Product Holding   |CA_FLAG                 		|Has a current account at the reporting time                                                                             			   |
|                  |CC_FLAG                 		|Has a credit card at the reporting time                                                                                 			   |
|                  |AUTO_LOAN_FLAG          		|Has an auto loan at the reporting time. Definition: has a loan balance > 0 (excluding bad debt and write off cases)     			   |
|                  |BUSINESS_LOAN_FLAG      		|Has a business loan at the reporting time. Definition: has a loan balance > 0 (excluding bad debt and write off cases)  			   |
|                  |MORTGAGE_LOAN_FLAG      		|Has a mortgage loan at the reporting time. Definition: has a loan balance > 0 (excluding bad debt and write off cases)  			   |
|                  |SECURED_LOAN_FLAG       		|Has a secured loan at the reporting time. Definition: has a loan balance > 0 (excluding bad debt and write off cases)   			   |
|                  |UNSECURED_LOAN_FLAG     		|Has an unsecured loan at the reporting time. Definition: has a loan balance > 0 (excluding bad debt and write off cases)			   |
|                  |LOAN_FLAG               		|Has any loan at the reporting time                                                                                      			   |
|                  |SAVING_FLAG          		|Has a Savings account at the reporting time                                                                             			   |
|                  |CIF_MOB                 		|Months since CIF opened until the reporting date                                                                        			   |
|                  |TD_FLAG                 		|Has Term Deposit and Savings account at the reporting time                                                              			   |
|                  |EBANK_MOB      		        |Months since ebank first opened until the reporting date                                                                			   |
|Product Open      |LAST_AUTO_LOAN_VALUE    		|Value of the most recent auto loan contract                                                                             			   |
|                  |LAST_AUTO_OPENED_DATE   		|Number of days from the most recent auto loan contract opening date to the reporting date                               			   |
|                  |LAST_BUSINESS_LOAN_VALUE		|Value of the most recent business loan contract                                                                         			   |
|                  |LAST_BUSINESS_OPENED_DATE		|Number of days from the most recent business loan contract opening date to the reporting date                           			   |
|                  |LAST_LOAN_VALUE         		|Value of the most recent loan contract                                                                                  			   |
|                  |LAST_LOAN_OPENED_DATE   		|Number of days from the most recent loan contract opening date to the reporting date                                    			   |
|                  |LAST_MORTGAGE_LOAN_VALUE		|Value of the most recent mortgage loan contract                                                                         			   |
|                  |LAST_MORTGAGE_OPENED_DATE		|Number of days from the most recent mortgage loan contract opening date to the reporting date                           			   |
|                  |LAST_SCL_LOAN_VALUE     		|Value of the most recent secured loan contract                                                                          			   |
|                  |LAST_SCL_OPENED_DATE    		|Number of days from the most recent secured loan contract opening date to the reporting date                            			   |
|                  |LAST_UL_LOAN_VALUE      		|Value of the most recent unsecured loan contract                                                                        			   |
|                  |LAST_UL_OPENED_DATE     		|Number of days from the most recent unsecured loan contract opening date to the reporting date                          			   |
|                  |MONTHS_SINCE_LAST_AUTO  		|Months since the most recent auto loan contract opened until the reporting date                                         			   |
|                  |MONTHS_SINCE_LAST_BUSINESS		|Months since the most recent business loan contract opened until the reporting date                                     			   |
|                  |MONTHS_SINCE_LAST_LOAN  		|Months since the most recent loan contract opened until the reporting date                                              			   |
|                  |MONTHS_SINCE_LAST_MORTGAGE		|Months since the most recent mortgage loan contract opened until the reporting date                                     			   |
|                  |MONTHS_SINCE_LAST_SCL   		|Months since the most recent secured loan contract opened until the reporting date                                      			   |
|                  |MONTHS_SINCE_LAST_UL    		|Months since the most recent unsecured loan contract opened until the reporting date                                    			   |
|                  |CIF_OPEN_CHANNEL        		|CIF creation channel                                                                                                    			   |
|                  |EBANK_CHANNEL_GROUP     		|e-banking opening channel group (first time)                                                                            			   |
|                  |EBANK_FIRST_OPEN_CHANNEL		|e-banking first opening channel                                                                                         			   |
|                  |CIF_OPEN_DATE           		|Date when CIF was created                                                                                              			   |
|                  |EBANK_FIRST_OPEN_DATE   		|Date when ebank account was first created                                                                              			   |
|                  |MB2_FIRST_OPEN_DATE     		|Date when app 2.0 account was first created                                                                            			   |
|                  |MB2_FIRST_CHANNEL       		|Channel used to create app 2.0 account for the first time                                                              			   |
|                  |MB2_CHANNEL_GROUP       		|Channel group used to create app 2.0 account for the first time                                                        			   |
|Product Usage     |AVGBAL_AUTO_LOAN_12M    		|Average auto loan balance in the past 12 months                                                                         			   |
|                  |AVGBAL_BUSINESS_LOAN_12M		|Average business loan balance in the past 12 months                                                                     			   |
|                  |AVGBAL_CS_12M           		|Average casa (current account and savings account) balance in the past 12 months                                        			   |
|                  |AVGBAL_LOAN_12M         		|Average loan balance in the past 12 months                                                                              			   |
|                  |AVGBAL_LOAN_3M          		|Average loan balance in the past 3 months                                                                               			   |
|                  |AVGBAL_LOAN_6M          		|Average loan balance in the past 6 months                                                                               			   |
|                  |AVGBAL_LOAN_9M          		|Average loan balance in the past 9 months                                                                               			   |
|                  |AVGBAL_MORTGAGE_LOAN_12M		|Average mortgage loan balance in the past 12 months                                                                     			   |
|                  |AVGBAL_SCL_LOAN_12M     		|Average secured loan balance in the past 12 months                                                                      			   |
|                  |AVGBAL_TD_12M           		|Average term deposit balance in the past 12 months                                                                      			   |
|                  |AVGBAL_UL_LOAN_12M      		|Average unsecured loan balance in the past 12 months                                                                    			   |
|                  |CURBAL_AUTO_LOANS       		|Current balance of auto loans                                                                                           			   |
|                  |CURBAL_BUSINESS_LOANS   		|Current balance of business loans                                                                                       			   |
|                  |CURBAL_LOANS            		|Current balance of all loans                                                                                            			   |
|                  |CURBAL_MORTGAGE_LOANS   		|Current balance of mortgage loans                                                                                       			   |
|                  |CURBAL_SECURED_LOANS    		|Current balance of secured loans                                                                                        			   |
|                  |CURBAL_UNSECURED_LOANS  		|Current balance of unsecured loans                                                                                      			   |
|                  |DIGI_FLAG               		|Has a Digi current account at the reporting time                                                                        			   |
|                  |EBANK_FLAG              		|Has e-banking at the reporting time                                                                                     			   |
|                  |TOTAL_AUTO_VALUE        		|Total value of all auto loans                                                                                           			   |
|                  |TOTAL_BUSINESS_VALUE    		|Total value of all business loans                                                                                       			   |
|                  |TOTAL_LOAN_COUNT        		|Total count of all loans                                                                                                			   |
|                  |TOTAL_LOAN_VALUE        		|Total value of all loans                                                                                                			   |
|                  |TOTAL_MORTGAGE_VALUE    		|Total value of all mortgage loans                                                                                       			   |
|                  |TOTAL_SCL_VALUE         		|Total value of all secured loans                                                                                        			   |
|                  |TOTAL_UL_VALUE          		|Total value of all unsecured loans                                                                                      			   |
|                  |DAYS_SINCE_LAST_ACTIVE  		|Number of days since the last Active date until the reporting date                                   						   |
|                  |VIB_CARE_INSURANCE_CNT_3M		|Number of times users used  Care Insurance feature in the last 3 months                                                			   |
|                  |VIEW_ACCOUNT_INFO_DAY_CNT_3M	|Number of days users viewed account information feature in the last 3 months                                           			   |
|                  |ACCOUNT_MANAGEMENT_DAY_CNT_3M	|Number of days users used account management feature in the last 3 months                                              			   |
|                  |LOAN_MANAGEMENT_DAY_CNT_3M		|Number of days users used loan management feature in the last 3 months                                                 			   |
|                  |CREDIT_CARD_MANAGEMENT_DAY_CNT_3M	|Number of days users used credit card management feature in the last 3 months                                          			   |
|                  |MORE_USAGE_DAY_CNT_3M   		|Number of days users used more usage feature in the last 3 months                                                      			   |
|                  |SECURITY_DAY_CNT_3M     		|Number of days users used security feature in the last 3 months                                                        			   |
|                  |AR_DAY_CNT_3M           		|Number of days users used AR feature in the last 3 months                                                              			   |
|                  |PIGGY_DAY_CNT_3M        		|Number of days users used Piggy feature in the last 3 months                                                           			   |
|                  |VOICEBOT_DAY_CNT_3M     		|Number of days users used Voicebot feature in the last 3 months                                                        			   |
|                  |VIB_CARE_INSURANCE_DAY_CNT_3M	|Number of days users used  Care Insurance feature in the last 3 months                                                 			   |
|                  |VIEW_ACCOUNT_INFO_CNT_1M		|Number of times users viewed their account information within the last month                                           			   |
|                  |ACCOUNT_MANAGEMENT_CNT_1M		|Number of times users managed their account within the last month                                                      			   |
|                  |LOAN_MANAGEMENT_CNT_1M  		|Number of times users managed their loan within the last month                                                         			   |
|                  |CREDIT_CARD_MANAGEMENT_CNT_1M	|Number of times users managed their credit card within the last month                                                  			   |
|                  |MORE_USAGE_CNT_1M       		|Number of times users accessed additional features within the last month                                               			   |
|                  |SECURITY_CNT_1M         		|Number of times users accessed security features within the last month                                                 			   |
|                  |AR_CNT_1M               		|Number of times users accessed accounts receivable features within the last month                                      			   |
|                  |PIGGY_CNT_1M            		|Number of times users accessed Piggy features within the last month                                                    			   |
|                  |VOICEBOT_CNT_1M         		|Number of times users used voicebot within the last month                                                              			   |
|                  |VIB_CARE_INSURANCE_CNT_1M		|Number of times users accessed  care insurance features within the last month                                          			   |
|                  |VIEW_ACCOUNT_INFO_DAY_CNT_1M	|Number of days users viewed their account information within the last month                                         	  			   |
|                  |ACCOUNT_MANAGEMENT_DAY_CNT_1M	|Number of days users managed their account within the last month                                                       			   |
|                  |LOAN_MANAGEMENT_DAY_CNT_1M		|Number of days users managed their loan within the last month                                                          			   |
|                  |CREDIT_CARD_MANAGEMENT_DAY_CNT_1M	|Number of days users managed their credit card within the last month                                                   			   |
|                  |MORE_USAGE_DAY_CNT_1M   		|Number of days users accessed additional features within the last month                                                			   |
|                  |SECURITY_DAY_CNT_1M     		|Number of days users accessed security features within the last month                                                  			   |
|                  |AR_DAY_CNT_1M           		|Number of days users accessed accounts receivable features within the last month                                       			   |
|                  |PIGGY_DAY_CNT_1M        		|Number of days users accessed Piggy features within the last month                                                     			   |
|                  |VOICEBOT_DAY_CNT_1M     		|Number of days users used voicebot within the last month                                                               			   |
|                  |VIB_CARE_INSURANCE_DAY_CNT_1M	|Number of days users accessed  care insurance features within the last month                                           			   |
|                  |LOGIN_MB2_DAY_CNT_1M    		|Number of days users logged into app 2.0 app within the last month                                                     			   |
|                  |LOGIN_MB1_DAY_CNT_1M    		|Number of days users logged into app 1.0 app (including Quickview) within the last month                               			   |
|                  |TRANS_DAY_CNT_1M        		|Number of days with digital transactions within the last month                                                         			   |
|                  |QUICKVIEW_MB2_DAY_CNT_1M		|Number of days users accessed the Quickview feature in the app 2.0 app within the last month                           			   |
|                  |ACTIVE_DAY_CNT_1M       		|Number of active days (according to OKR definition) within the last month                                              			   |
|Transaction       |CASH_DEPOSIT_AMT_12M    		|Amount of cash deposit transactions in the past 12 months                                                               			   |
|                  |CASH_DEPOSIT_CNT_12M    		|Count of cash deposit transactions in the past 12 months                                                                			   |
|                  |CASH_WITHDRAWAL_AMT_12M 		|Amount of cash withdrawal transactions in the past 12 months                                                            			   |
|                  |CASH_WITHDRAWAL_CNT_12M 		|Count of cash withdrawal transactions in the past 12 months                                                             			   |
|                  |CC_SPENDING_AMT_ECOM_12M		|Amount spent on E-commerce transactions from credit card accounts in the past 12 months                                 			   |
|                  |CC_SPENDING_CNT_ECOM_12M		|Count of E-commerce transactions from credit card accounts in the past 12 months                                        			   |
|                  |CC_SPENDING_AMT_CASH_12M		|Amount spent on cash/ATM channels from credit card accounts in the past 12 months                                       			   |
|                  |CC_SPENDING_CNT_CASH_12M		|Count of cash/ATM transactions from credit card accounts in the past 12 months                                          			   |
|                  |CC_SPENDING_AMT_POS_12M 		|Amount spent on POS transactions from credit card accounts in the past 12 months                                        			   |
|                  |CC_SPENDING_CNT_POS_12M 		|Count of POS transactions from credit card accounts in the past 12 months                                               			   |
|                  |CREDIT_TXN_AMT_12M      		|Amount of credit transactions in the past 12 months                                                                     			   |
|                  |CREDIT_TXN_CNT_12M      		|Count of credit transactions in the past 12 months                                                                      			   |
|                  |DEDIT_TXN_AMT_12M       		|Total amount of debit transactions in the last 12 months                                                                			   |
|                  |DEDIT_TXN_CNT_12M       		|Total number of debit transactions in the last 12 months                                                                			   |
|                  |EBANK_AMT_12M           		|Total amount of ebank transactions in the last 12 months                                                                			   |
|                  |EBANK_CNT_12M           		|Total number of ebank transactions in the last 12 months                                                                			   |
|                  |EBANK_IB_CHANNEL_AMT_12M		|Total amount of online transactions on Internet Banking (Website...) in the last 12 months                              			   |
|                  |EBANK_IB_CHANNEL_CNT_12M		|Total number of online transactions on Internet Banking (Website...) in the last 12 months                              			   |
|                  |EBANK_MB_CHANNEL_AMT_12M		|Total amount of online transactions on APPs (app) in the last 12 months                                                 			   |
|                  |EBANK_MB_CHANNEL_CNT_12M		|Total number of online transactions on APPs (app) in the last 12 months                                                 			   |
|                  |EBANK_OTHER_CHANNEL_AMT_12M		|Total amount of online transactions outside IB/MB in the last 12 months                                                 		   	   |
|                  |EBANK_OTHER_CHANNEL_CNT_12M		|Total number of online transactions outside IB/MB in the last 12 months                                                 			   |
|                  |EBANK_PAYMENT_AMT_12M   		|Total amount of online payments in the last 12 months                                                                   			   |
|                  |EBANK_PAYMENT_CNT_12M   		|Total number of online payment transactions in the last 12 months                                                       			   |
|                  |EBANK_TOPUP_AMT_12M     		|Total amount of online top-up transactions in the last 12 months                                                        			   |
|                  |EBANK_TOPUP_CNT_12M     		|Total number of online top-up transactions in the last 12 months                                                        			   |
|                  |EBANK_TRANSFER_AMT_12M  		|Total amount of online transfer transactions in the last 12 months                                                      			   |
|                  |EBANK_TRANSFER_CNT_12M  		|Total number of online transfer transactions in the last 12 months                                                      			   |
|                  |LAST_EB_TRANS_DAYS      		|Number of days from the last ebank transaction to the reporting date                                                    			   |
|                  |TRANSFER_CREDIT_AMT_12M 		|Total value of credit transfer transactions in the last 12 months                                                       			   |
|                  |TRANSFER_CREDIT_CNT_12M 		|Total number of credit transfer transactions in the last 12 months                                                      			   |
|                  |TRANSFER_DEBIT_AMT_12M  		|Total value of debit transfer transactions in the last 12 months                                                        			   |
|                  |TRANSFER_DEBIT_CNT_12M  		|Total number of debit transfer transactions in the last 12 months                                                       			   |
|                  |MB2_TRANS_CNT_3M        		|Number of transactions on app 2.0 app in the last 3 months                                                             			   |
|                  |MB2_TRANS_AMT_3M        		|Total transaction amount on app 2.0 app in the last 3 months                                                           			   |
|                  |MB2_TF_TRANS_CNT_3M     		|Number of transfer transactions on app 2.0 app in the last 3 months                                                    			   |
|                  |MB2_TF_TRANS_AMT_3M     		|Total transfer transaction amount on app 2.0 app in the last 3 months                                                  			   |
|                  |MB2_BP_TRANS_CNT_3M     		|Number of payment transactions on app 2.0 app in the last 3 months                                                     			   |
|                  |MB2_BP_TRANS_AMT_3M     		|Total payment transaction amount on app 2.0 app in the last 3 months                                                   			   |
|                  |MB2_TO_TRANS_CNT_3M     		|Number of top-up transactions on app 2.0 app in the last 3 months                                                      			   |
|                  |MB2_TO_TRANS_AMT_3M     		|Total top-up transaction amount on app 2.0 app in the last 3 months                                                    			   |
|                  |MB2_TRANS_CNT_6M        		|Number of transactions on app 2.0 app in the last 6 months                                                             			   |
|                  |MB2_TRANS_AMT_6M        		|Total transaction amount on app 2.0 app in the last 6 months                                                           			   |
|                  |MB2_TF_TRANS_CNT_6M     		|Number of transfer transactions on app 2.0 app in the last 6 months                                                    			   |
|                  |MB2_TF_TRANS_AMT_6M     		|Total transfer transaction amount on app 2.0 app in the last 6 months                                                  			   |
|                  |MB2_BP_TRANS_CNT_6M     		|Number of payment transactions on app 2.0 app in the last 6 months                                                     			   |
|                  |MB2_BP_TRANS_AMT_6M     		|Total payment transaction amount on app 2.0 app in the last 6 months                                                   			   |
|                  |MB2_TO_TRANS_CNT_6M     		|Number of top-up transactions on app 2.0 app in the last 6 months                                                      			   |
|                  |MB2_TO_TRANS_AMT_6M     		|Total top-up transaction amount on app 2.0 app in the last 6 months                                                    			   |
|                  |CC_SPENDING_AMT_12M     		|Total spending amount from credit card account in the last 12 months                                                   			   |
|                  |CC_SPENDING_CNT_12M     		|Number of transactions from credit card account in the last 12 months                                                  			   |
|                  |CC_SPENDING_AMT_ECOM_3M 		|Total spending amount on E-commerce from credit card account in the last 3 months                                      			   |
|                  |CC_SPENDING_CNT_ECOM_3M 		|Number of E-commerce transactions from credit card account in the last 3 months                                        			   |
|                  |CC_SPENDING_AMT_CASH_3M 		|Total spending amount through cash/ATM channels from credit card account in the last 3 months                          			   |
|                  |CC_SPENDING_CNT_CASH_3M 		|Number of cash/ATM transactions from credit card account in the last 3 months                                          			   |
|                  |CC_SPENDING_AMT_POS_3M  		|Total spending amount on POS machines from credit card account in the last 3 months                                    			   |
|                  |CC_SPENDING_CNT_POS_3M  		|Number of POS transactions from credit card account in the last 3 months                                               			   |
|                  |CC_SPENDING_AMT_3M      		|Total spending amount from credit card account in the last 3 months                                                    			   |
|                  |CC_SPENDING_CNT_3M      		|Number of transactions from credit card account in the last 3 months                                                   			   |
|                  |CC_SPENDING_AMT_ECOM_6M 		|Total spending amount on E-commerce from credit card account in the last 6 months                                      			   |
|                  |CC_SPENDING_CNT_ECOM_6M 		|Number of E-commerce transactions from credit card account in the last 6 months                                        			   |
|                  |CC_SPENDING_AMT_CASH_6M 		|Total spending amount through cash/ATM channels from credit card account in the last 6 months                          			   |
|                  |CC_SPENDING_CNT_CASH_6M 		|Number of cash/ATM transactions from credit card account in the last 6 months                                          			   |
|                  |CC_SPENDING_AMT_POS_6M  		|Total spending amount on POS machines from credit card account in the last 6 months                                    			   |
|                  |CC_SPENDING_CNT_POS_6M  		|Number of POS transactions from credit card account in the last 6 months                                               			   |
|                  |CC_SPENDING_AMT_6M      		|Total spending amount from credit card account in the last 6 months                                                    			   |
|                  |CC_SPENDING_CNT_6M      		|Number of transactions from credit card account in the last 6 months                                                   			   |
|                  |DEBIT_TXN_AMT_12M       		|Total debit transaction amount in the past 12 months                                                                   			   |
|                  |DEBIT_TXN_CNT_12M       		|Total number of debit transactions in the past 12 months                                                               			   |
|                  |CREDIT_TXN_AMT_3M       		|Total credit transaction amount in the past 3 months                                                                   			   |
|                  |CREDIT_TXN_CNT_3M       		|Total number of credit transactions in the past 3 months                                                               			   |
|                  |DEBIT_TXN_AMT_3M        		|Total debit transaction amount in the past 3 months                                                                    			   |
|                  |DEBIT_TXN_CNT_3M        		|Total number of debit transactions in the past 3 months                                                                			   |
|                  |CREDIT_TXN_AMT_6M       		|Total credit transaction amount in the past 6 months                                                                   			   |
|                  |CREDIT_TXN_CNT_6M       		|Total number of credit transactions in the past 6 months                                                               			   |
|                  |DEBIT_TXN_AMT_6M        		|Total debit transaction amount in the past 6 months                                                                    			   |
|                  |DEBIT_TXN_CNT_6M        		|Total number of debit transactions in the past 6 months                                                                			   |
|                  |CREDIT_TXN_AMT_9M       		|Total credit transaction amount in the past 9 months                                                                   			   |
|                  |CREDIT_TXN_CNT_9M       		|Total number of credit transactions in the past 9 months                                                               			   |
|                  |DEBIT_TXN_AMT_9M        		|Total debit transaction amount in the past 9 months                                                                    			   |
|                  |DEBIT_TXN_CNT_9M        		|Total number of debit transactions in the past 9 months                                                                			   |


#### Methodology
The machine learning model conducted in the study is as follows.

**Logistic Regression**: In logistic regression, a logit transformation is applied on the odds—that is, the probability of success divided by the probability of failure. This is also commonly known as the log odds, or the natural logarithm of odds. The beta parameter, or coefficient, in this model is commonly estimated via maximum likelihood estimation (MLE). This method tests different values of beta through multiple iterations to optimize for the best fit of log odds. All of these iterations produce the log likelihood function, and logistic regression seeks to maximize this function to find the best parameter estimate. Once the optimal coefficient (or coefficients if there is more than one independent variable) is found, the conditional probabilities for each observation can be calculated, logged, and summed together to yield a predicted probability.

**KNN**: The initial model introduced in the subsequent paragraph is K-Nearest Neighbor (KNN). Based on the K-Nearest Neighbors (KNN) algorithm, data points with similar characteristics tend to cluster together in a given space. Consequently, when faced with an undefined observation, the determination of its label relies on the conditional probability derived from neighboring observations. In order to differentiate the unspecified observation, the K-nearest neighbors (KNN) algorithm utilizes a collection of K coefficients (where K is a positive integer) that represent the number of neighboring observations. One approach for determining the spatial separation between neighborhoods in order to categorize an unspecified point and a point requiring definition is through the utilization of Euclidean distance (Makruf et al., 2021). The K coefficient exerts a significant impact on the classification outcomes of the K-nearest neighbors (KNN) model. A model characterized by a low value of K exhibits a greater degree of flexibility, albeit at the risk of overfitting. Conversely, a model with a larger value of K possesses reduced flexibility and may potentially overlook certain information included within the dataset. Hence, the choice of the K coefficient holds significant importance inside the K-nearest neighbors (KNN) model.

**Random forest**: The utilization of a decision tree is commonly observed in the context of inductive inference. Furthermore, the utilization of this approach extends to the evaluation of discrete-valued functions in the presence of noise, as well as the acquisition of knowledge pertaining to inconsistent phrases (Bardab et al., 2021). The principle of reducing variance by aggregating several decision trees is applied in the Random Forest algorithm, where individual decision trees are evaluated and subsequently combined to form a final composite decision tree. The outcome of each decision tree inside a random forest is inherently distinct due to the use of random components, such as random samples and random sets of characteristics, in the process of constructing decision trees. The random forest ensemble consists of many decision trees, each employing a decision tree method with distinct datasets and feature sets. The outcome of the random forest model is derived from the collective predictions of the aforementioned decision trees (Nohuddin et al., 2021).Due to the limited consideration of all dataset attributes by a single decision tree technique, the resulting model may exhibit either overfitting or underfitting. Nevertheless, this problem can be effectively addressed through the utilization of a random forest algorithm. This algorithm employs a collective aggregation of information from multiple decision trees, resulting in a random forest model that exhibits both low bias and low variance. Consequently, the performance of the random forest model surpasses that of alternative approaches.

**Gradient boosting**: The development of boosting was motivated by the desire to address the constraints of earlier weak hypotheses or models. Boosting involves the creation of many models that aim to complement one another. Specifically, subsequent models in the boosting process are designed to learn from the mistakes made by earlier models, hence improving overall performance. Furthermore, models possess their own set of weighted coefficients, which can be modified using various optimization techniques. Hence, the Boosting algorithm is inherently sequential in nature, precluding the possibility of parallelization and consequently resulting in a somewhat longer training period for the model. Following the completion of each iteration, it is quite probable that Boosting will result in an exponential reduction of the error for the model.

The process is conducted with following steps:
- Step 1: defining the purpose of analytics. The purpose would be aligned with the research question.
- Step 2: defining sampling window. There are three windows to consider
	- Sampling window: the time frame during which the customers are sampled. We choose duration customers opening CIF before 1/1/2023.
	- Observation window: the time frame during which the customers' behavior are observed. We observe customers' behavior from 1/1/2023 to 9/30/2023.
	- Evaluation window: the time frame during which the customers' behavior are evaluated as churn or not. We label customers as churn or not during 10/1/2023 and 10/31/2023.
- Step 3: defining outcome of machine learning models.
- Step 4: conducting exploratory data analysis (EDA). The EDA are processed as follows.
	- Check for missing values and outliers
	- Explore the distribution of variables
	- Analyze relationships between variables
	- Visualize data using graphs and charts
	- Identify patterns and trends in the data
- Step 5: feature engineering
	- Perform feature selection to identify relevant features
	- Create new features using existing data
	- Normalize or standardize numerical features
	- Encode categorical features using one-hot encoding or label encoding
	- Handle imbalance dataset
	- Split data into training and test sets
- Step 6: modeling with machine learning algorithms
	- Split data with stratified sampling into training set (70%) and testing set (30%).
	- Choose algorithms for study: Logistic regression, kNN, Random Forest, Gradient Boosting
	- Validation method: 5-fold cross validation using grid search approach on `accuracy` scores.
- Step 7: evaluating models based on 
	- Precision
	- Recall
	- F1-score


#### Results

The dataset initially 1,845,792 observed customers and reduces to 1,757,896 customers for all 149 variables after excluding all customers below 18 years old having ebank account and available in mobile app. Around 65% of dataset is labeled 1 for independent variable.

After EDA, we end up following independent variables for models. The other variables whose absolute correlation coefficient larger than 0.7 is excluded.

|Feature        	 |Description             													|
|------------------------|------------------------------------------------------------------------------------------------------------------------------|
|CIF_OPEN_CHANNEL	 |CIF creation channel    													|
|EBANK_FIRST_OPEN_CHANNEL|e-banking first opening channel   												|
|EBANK_CHANNEL_GROUP	 |e-banking opening channel group (first time)   										|
|GENDER         	 |Gender                     													|
|AGE             	 |Customer age               													|
|MB2_FIRST_CHANNEL	 |Channel used to create app 2.0 account for the first time   									|
|MB2_CHANNEL_GROUP	 |Channel group used to create app 2.0 account for the first time   								|
|EBANK_FLAG     	 |Has e-banking at the reporting time   											|
|LOGIN_MB2_DAY_CNT_1M	 |Number of days users logged into app 2.0 app within the last month   								|
|LOGIN_MB1_DAY_CNT_1M	 |Number of days users logged into app 1.0 app (including Quickview) within the last month   					|
|CC_FLAG        	 |Has a credit card at the reporting time   											|
|CC_SPENDING_AMT_12M	 |Total spending amount from credit card account in the last 12 months   							|
|CC_SPENDING_AMT_ECOM_12M|Amount spent on E-commerce transactions from credit card accounts in the past 12 months   					|
|CC_SPENDING_AMT_CASH_12M|Amount spent on cash/ATM channels from credit card accounts in the past 12 months   						|
|CC_SPENDING_CNT_POS_12M |Count of POS transactions from credit card accounts in the past 12 months   							|
|CC_SPENDING_CNT_ECOM_12M|Count of E-commerce transactions from credit card accounts in the past 12 months   						|
|CA_FLAG        	 |Has a current account at the reporting time   										|
|TD_FLAG        	 |Has Term Deposit and Savings account at the reporting time   									|
|DIGI_FLAG      	 |Has a Digi current account at the reporting time   										|
|MB2_TRANS_CNT_3M	 |Number of transactions on app 2.0 app in the last 3 months   									|
|MB2_TRANS_AMT_3M	 |Total transaction amount on app 2.0 app in the last 3 months   								|
|MB2_BP_TRANS_CNT_3M	 |Number of payment transactions on app 2.0 app in the last 3 months   								|
|MB2_BP_TRANS_AMT_3M	 |Total payment transaction amount on app 2.0 app in the last 3 months   							|
|MB2_TO_TRANS_CNT_3M	 |Number of top-up transactions on app 2.0 app in the last 3 months   								|
|MB2_TO_TRANS_AMT_3M	 |Total top-up transaction amount on app 2.0 app in the last 3 months   							|
|TOTAL_LOAN_CNT_2023	 |Total loan items in 2023   													|
|TOTAL_LOAN_AMT_2023	 |Total loan amount in 2023   													|
|AUTO_LOAN_AMT_2023	 |Total auto loan amount in 2023   												|
|BUSINESS_LOAN_AMT_2023	 |Total business loan amount in 2023   												|
|SECURED_LOAN_AMT_2023	 |Total secured loan amount in 2023   												|
|UNSECURED_LOAN_AMT_2023 |Total unsecured loan amount in 2023   											|
|LOAN_FLAG      	 |Has any loan at the reporting time   												|
|AUTO_LOAN_FLAG 	 |Has an auto loan at the reporting time. Definition: has a loan balance > 0 (excluding bad debt and write off cases)		|
|MORTGAGE_LOAN_FLAG	 |Has a mortgage loan at the reporting time. Definition: has a loan balance > 0 (excluding bad debt and write off cases)	|
|BUSINESS_LOAN_FLAG	 |Has a business loan at the reporting time. Definition: has a loan balance > 0 (excluding bad debt and write off cases)	|
|SECURED_LOAN_FLAG 	 |Has a secured loan at the reporting time. Definition: has a loan balance > 0 (excluding bad debt and write off cases)		|
|UNSECURED_LOAN_FLAG	 |Has an unsecured loan at the reporting time. Definition: has a loan balance > 0 (excluding bad debt and write off cases)	|
|CURBAL_LOANS   	 |Current balance of all loans   												|


The result after modelling phase is as follows. Please note that KNN requires more computational attempt and hence it is excluded from the study consideration.

|Model              |Best specification                        |Training performance	    		      |Testing performance			    |
|                   |                                          |----------------------------------------------|---------------------------------------------|
|                   |                                          |Accuracy            |Precision|Recall|F1-score|Accuracy           |Precision|Recall|F1-score|
|-------------------|------------------------------------------|--------------------|---------|------|--------|-------------------|---------|------|--------|
|Logistic regression|-                                         |0.92                |0.87     |0.98  |0.92    |0.94               |0.93     |0.98  |0.95    |
|Random forest      |`{'max_depth': 6, 'max_features': 'sqrt'}`|0.94                |0.94     |0.94  |0.94    |0.94               |0.97     |0.94  |0.95    |
|Gradient Boosting  |`{'max_depth': 6, 'max_features': 'sqrt'}`|0.94                |0.94     |0.96  |0.95    |0.95               |0.96     |0.95  |0.96    |

In summary, all three models exhibit strong performance, with Gradient Boosting showing a slight edge in terms of testing metrics. The choice between these models would depend on various factors such as interpretability, computational cost, and the specific goals of the task. It's crucial to consider these aspects before deciding on the final model for deployment.

**Model Comparison:**
- All three models exhibit high accuracy and perform well in the training and testing datasets.
- Random Forest and Gradient Boosting consistently outperform Logistic Regression across all metrics. With Gradient Boosting, the F1-score is slightly better.

**Overfitting:**
- The models seem to generalize well as there is minimal difference between training and testing performance, indicating low overfitting.

**Feature Importance:**
- Understanding the importance of features in Random Forest and Gradient Boosting models could provide insights into factors influencing customer churn.

Following is the feature importance produced by Gradient Boosting model in the ascending order, based on SHAP values.

|Feature            		|Importance order  	|Description																	|
|-------------------------------|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
|LOGIN_MB2_DAY_CNT_1M		|1           		|Number of days users logged into app within the last month											|
|CREDIT_CARD_MANAGEMENT_CNT_3M	|2           		|Frequency that customer view credit card management in app											|
|CA_FLAG            		|3           		|Has a current account at the reporting time													|
|CC_FLAG            		|4           		|Has a credit card at the reporting time													|
|MORE_USAGE_DAY_CNT_3M		|5           		|Number of distinct days that customer view other than account information, account information, loan management, credit card management in app	|
|MORE_USAGE_CNT_3M  		|6           		|Frequency that customer view other than account information, account information, loan management, credit card management in app		|
|CREDIT_TXN_AMT_12M 		|7           		|Amount of credit transactions in the past 12 months												|
|CC_SPENDING_AMT_ECOM_12M	|8           		|Amount spent on E-commerce transactions from credit card accounts in the past 12 months							|
|AGE                		|9           		|Customer age																	|
|MB2_TRANS_CNT_3M   		|10          		|Number of transactions on app 2.0 app in the last 3 months											|
|MB2_BP_TRANS_CNT_3M		|11          		|Number of payment transactions on app 2.0 app in the last 3 months										|
|CC_SPENDING_AMT_12M		|12          		|Total spending amount from credit card account in the last 12 months										|
|TD_FLAG            		|13          		|Has Term Deposit and Savings account at the reporting time											|
|CC_SPENDING_CNT_POS_12M	|14          		|Count of POS transactions from credit card accounts in the past 12 months									|
|MB2_TO_TRANS_CNT_3M		|15          		|Number of top-up transactions on app 2.0 app in the last 3 months										|
|VIEW_ACCOUNT_INFO_CNT_3M	|16          		|Frequency that customer view account information in app											|
|CIF_OPEN_CHANNEL_MYVIB		|17          		|CIF creation channel: Organic       														|
|SECURITY_CNT_3M    		|18          		|Frequency that customer view security functions in app												|
|EBANK_CHANNEL_GROUP_MYVIB	|19          		|e-banking opening channel group (first time): Organic       											|
|MB2_TRANS_AMT_3M   		|20          		|Total transaction amount on app 2.0 app in the last 3 months											|

Accordingly, there are several assumptions can be safely formulated.
- **Frequency of App Usage:** The most crucial factor contributing to churn prediction is the number of days users log into the app within the last month (`LOGIN_MB2_DAY_CNT_1M`). Higher login frequency might suggest engagement and satisfaction, while lower frequency could indicate disinterest or issues with the app.

- **Credit Card Management:** The frequency of viewing credit card management in the app (`CREDIT_CARD_MANAGEMENT_CNT_3M`) and the presence of a credit card (`CC_FLAG`) are significant. Customers who actively manage their credit cards within the app and use credit cards might have a higher likelihood of retention.

- **Account Type:** Having a current account (`CA_FLAG`) and credit card (`CC_FLAG`) and term deposit (`TD_FLAG`) at the reporting time influences churn prediction. Customers with a diverse set of financial products are less likely to churn, as they are more deeply integrated into the banking ecosystem.

- **Exploration of App Features:** More frequent exploration of features beyond basic account information and management (`MORE_USAGE_DAY_CNT_3M`, `MORE_USAGE_CNT_3M`) is associated with lower churn. This suggests that users who explore additional app functionalities are more likely to stay engaged.

- **Credit Transactions:** The amount of credit transactions in the past 12 months (`CREDIT_TXN_AMT_12M`) and spending on E-commerce transactions from credit card accounts (`CC_SPENDING_AMT_ECOM_12M`) are relevant factors. Higher credit activity and online spending might indicate a customer's reliance on the bank's credit services.

- **Customer Demographics:** Age (`AGE`) plays a role in churn prediction. Different age groups may have distinct preferences and needs, influencing their likelihood to churn.

- **App Transaction Metrics:** Metrics related to app transactions, such as the number of transactions (`MB2_TRANS_CNT_3M`) and top-up transactions (`MB2_TO_TRANS_CNT_3M`), contribute to churn prediction. Higher transactional activity suggests customer engagement.

- **Total Spending from Credit Card:** The total spending amount from the credit card account in the last 12 months (`CC_SPENDING_AMT_12M`) is a relevant factor. Higher spending may indicate a customer's dependence on credit facilities, impacting their decision to stay with the bank.

- **Security Functions:** The frequency of viewing security functions in the app (`SECURITY_CNT_3M`) is a factor. Customers who actively engage with security features might have a higher level of trust in the banking app.

- **Organic Account Creation:** The channels associated with organic activities (`CIF_OPEN_CHANNEL_MYVIB` and `EBANK_CHANNEL_GROUP_MYVIB`) play a role. Customers who joined through organic channels are less likely to churn.

#### Discussion

Predictive analytics can be leveraged to proactively identify and mitigate factors contributing to customer churn in the mobile application of Bank X by implementing the following strategies:

1. **User Engagement Campaigns:** Utilize predictive models to identify users at risk of churn based on low engagement metrics such as infrequent logins (`LOGIN_MB2_DAY_CNT_1M`). Launch targeted campaigns to encourage active app usage, possibly through personalized notifications, promotions, or incentives.

2. **Credit Card Management Support:** Offer personalized support and promotions to users who have a credit card (`CC_FLAG`) or engage frequently in credit card management activities (`CREDIT_CARD_MANAGEMENT_CNT_3M`). Provide educational content or exclusive offers to enhance the value of credit card usage.

3. **Enhanced App Features:** Focus on improving and promoting features related to account information (`VIEW_ACCOUNT_INFO_CNT_3M`), transactions (`MB2_TRANS_CNT_3M`), and top-up activities (`MB2_TO_TRANS_CNT_3M`). Regularly update the app to ensure a seamless and user-friendly experience.

4. **Financial Education and Assistance:** Identify users with low financial activity (`CREDIT_TXN_AMT_12M`, `CC_SPENDING_AMT_12M`) and implement educational campaigns or financial assistance programs to encourage more transactions and credit card usage.

5. **Targeted Marketing for E-commerce Users:** Launch targeted marketing campaigns for users who have significant spending on E-commerce transactions from credit card accounts (`CC_SPENDING_AMT_ECOM_12M`). Provide exclusive discounts or partnerships to retain these customers.

6. **Personalized Customer Service:** Tailor customer service interactions based on user demographics such as age (`AGE`) and the presence of various banking products (`CA_FLAG`, `CC_FLAG`, `TD_FLAG`). Address the unique needs and concerns of different customer segments.

7. **Security Awareness Initiatives:** Promote security features of the app (`SECURITY_CNT_3M`) and conduct awareness campaigns to assure users of the safety of their transactions. Communicate any updates or improvements in security protocols.

8. **Encourage Organic Channel Adoption:** Promote the benefits of organic channels for account creation (`CIF_OPEN_CHANNEL_MYVIB` and `EBANK_CHANNEL_GROUP_MYVIB`). Emphasize the advantages of choosing organic channels, such as better customer support or exclusive offers.

9. **Incentivize Unique App Usage:** Introduce loyalty programs or rewards for users who explore various app features (`MORE_USAGE_DAY_CNT_3M` and `MORE_USAGE_CNT_3M`). Encourage users to discover and use different sections of the app regularly.

10. **Regular Model Monitoring and Updates:** Continuously monitor the predictive model's performance and update it as needed. Regularly reevaluate the importance of features and adapt strategies based on changing customer behaviors and preferences.

11. **Feedback Loop and Continuous Improvement:** Establish a feedback loop where insights from customer interactions and churn predictions inform ongoing improvements in app features, services, and customer engagement strategies.

By incorporating these strategies, Bank X can use predictive analytics not only to identify customers at risk of churn but also to proactively implement targeted initiatives that address the specific factors influencing churn. This approach enables the bank to build stronger customer relationships, enhance user satisfaction, and ultimately reduce churn rates in its mobile banking application.

#### Next steps

For next steps, consider the following suggestions to further enhance the effectiveness of predictive analytics and customer retention strategies in the mobile application of Bank X:

1. **Early Warning System:** These models could be used as an early warning system to identify customers at risk of churning in the next month.

2. **Personalized Retention Strategies:** The model can help in devising personalized retention strategies for high-risk customers based on the features contributing to churn predictions.

3. **Resource Allocation:** By understanding the factors influencing churn, resources can be strategically allocated to address specific pain points or concerns of at-risk customers.

4. **Product Improvement:** Insights from the model can guide product improvement strategies, addressing issues that contribute to customer dissatisfaction.

5. **Customer Segmentation:** Utilize the model to segment customers based on their likelihood of churning, allowing for targeted marketing and engagement strategies for each segment.

6. **Real-time Monitoring:** Implement the model in a real-time monitoring system to continuously assess customer churn risk, enabling timely interventions.

7. **Feedback Loop:** Use the model predictions as part of a feedback loop to continuously update and improve the model's performance over time.

8. **Advanced Model Exploration**: Explore more advanced machine learning models or ensemble methods to improve predictive accuracy. Experiment with different algorithms, feature engineering techniques, and model architectures to identify the most effective approach.

#### Outline of project

- [Logistic Regression](/Notebooks/Training-SMOTE_Logistic.ipynb)
- [Random Forest](/Notebooks/Training_SMOTE_RF.ipynb)
- [Gradient Boosting](/Notebooks/Training-SMOTE_GradientBoosting.ipynb)

#### File structures

📦ChurnGuard
 ┣ 📂Models
 ┃ ┣ 📜Gradient_Boosting.sav
 ┃ ┣ 📜Logistic_regression.sav
 ┃ ┗ 📜RF.sav
 ┣ 📂Notebooks
 ┃ ┣ 📂Churn Prediction EDA Reports
 ┃ ┃ ┣ 📜.DS_Store
 ┃ ┃ ┣ 📜CUST_METRICS_ACTIVE_sweetviz.html
 ┃ ┃ ┣ 📜CUST_METRICS_CARD_sweetviz.html
 ┃ ┃ ┣ 📜CUST_METRICS_DEMOGRAPHIC.csv_sweetviz.html
 ┃ ┃ ┣ 📜CUST_METRICS_DEPO_SPOT_sweetviz.html
 ┃ ┃ ┣ 📜CUST_METRICS_DEPO_TRANS.csv_sweetviz.html
 ┃ ┃ ┣ 📜CUST_METRICS_EBANK_TRANS_sweetviz.html
 ┃ ┃ ┣ 📜CUST_METRICS_LENDING_BALANCE_2023_sweetviz.html
 ┃ ┃ ┣ 📜CUST_METRICS_LENDING_SPOT_sweetviz.html
 ┃ ┃ ┣ 📜CUST_METRICS_USAGE_sweetviz.html
 ┃ ┃ ┗ 📜SWEET_VIZ.py
 ┃ ┣ 📜Preprocessing.ipynb
 ┃ ┣ 📜Training-SMOTE_GradientBoosting.ipynb
 ┃ ┣ 📜Training-SMOTE_Logistic.ipynb
 ┃ ┗ 📜Training_SMOTE_RF.ipynb
 ┗ 📜ReadME.md


##### Contact and Further Information


