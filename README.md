DATASET:
https://www.kaggle.com/datasets/arpan129/insurance-fraud-detection?resource=download
  -synthetic data

GOAL:
  - To create a interface that asks for specific inputs to check if an insurance claim is or is not FRAUD through a logistic regression model.

PROCESS:
  EXCEL:
  - Used excel to clean up the initial dataset, removed unecessary variables and converted categorical variables into one-hot format.
  - As the data was incomplete, additional variables were added called "UNKOWN" instead of removing those data values.
  - Used AI to generate the IF excel statement code to make the process easier than manually typing everything.
  - Used a correlation table to determine the most important factors that influenced the claim to be FRAUD.
    
      -> Issues arised:
          - as the dataset is synthetic there were not enough strong correlations.
          - this led to the use of weakly correlating variables in the logistic regression model.

  RSTUDIO:
  - Used code to generate the logistic regression model through the glm function.
  - Learned how AIC indicated the effictiveness of a model.
  - Learned how to use the MASS library to find the best model through variables provided.
    
      -> Issues arised:
          - the incident type variable was split into 4 categories. Single, Theft, Parked and Multi. The Parked split variable was so insignificant it resulted in R considering it as a colinear variable.
            As a result, two variables had to be omitted when implenting the logistic regression function. This I believe is due to the data results being synthetic.
          - I realised too late that I didn't have to sort all the values out in an excel spreadsheet. I can use the factor function to convert multi-categorical variables into one-hot type. I assumed it was only for binary.

  PYTHON:
  - Wrote code to just ask for inputs that were entered into the equation, and then converted into a percentage to show as an output.
  - PANDAS library was not needed as model training was already completed in RSTUDIO
  - Most of the code is just for visual ease when entering values and options.
  - Github copilot assisted in fixing bugs and doing the repetitive parts of the code for me.

LIMITATIONS:
  - The dataset was for AMERICAN banks, this makes it not as relavent to Australian banks.
  - An attempt was made to find Australian banking data however that is not publically available.

FUTURE CONSIDERATIONS:
  - Use the factor function and compelte majority of data sorting in RSTUDIO
  - Learn how to implemenet pandas as well as RSTUDIO
  - Utilise a better dataset 
