# dengAI
Competition on Driven Data to predict Dengue Fever cases

[Dengue Competition - DriveData.com](https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/)

## Notes 12/17/20
### To Dos ()
### EDA
- Create visualizations of all X variables by time
### Research
- (C) Mosquito lifecycle - what is lag for factors increasing mosquito activity to dengue reported rates (i.e., X weeks after high rain, more cases occur?)
- (A) Are 'Reanalysis' columns duplicate/redundant with other weather station data (e.g., 3x precipitation metrics)?
### Data Cleaning
- (C) Encoding the 'City' column - Research whether to label encode vs. OH encode
- (A) See if the 'ndvi_ne' missing values and be imputed based off the other 3 values (train/test split)
### Modeling
- Evaluate any potential duplicated weather metrics for model performance
- Rerun regression models with encoded city and attempt feature selection (using LASSO or other)
- Attempt Random Forest Regression and Boosted Regression models