# Linear Regression For Predicting Admission In University Using Sklearn
#
![](/image/cover.png)

This is a multiple linear regression model built using sklearn to predict the chances of admission in university with an accuracy of 80% based on the following features :

* GRE Score 
* TOEFL Score 
* University Rating 
* Rating of Statement of Purpose(SOP)
* Rating of Letter of Recommendation(LOR)
* CGPA
* Research
#
source of dataset is https://www.kaggle.com/mohansacharya/graduate-admissions?select=Admission_Predict_Ver1.1.csv
#
## order of features that plays important role in predicting chance of admission :
```
CGPA (0.88) 
GRE Score (0.81)
TOEFL Score (0.79)
University Rating (0.69)
SOP (0.68)
LOR (0.65)
Research (0.55) 
```

=> CGPA is the highest correlated while Research is the least correlated. It means that CGPA plays an important role in deciding admission than any other feature here.
#
## Application Of This Prediction 
* It will save students time by giving them their chance of admission in a particular university so that they can decide on planning their admission procedure.
* As the prediction is solely dependent on certain academic records, so the candidate can know where they are lying in terms of academics.
* While plotting heatmap of the dataset, you can clearly see that certain features impacts more while predicting the chances than other. This will help student to know the weightage of each scores so they can plan accordingly. This way they can set their priorities.

## Comparison Between Actual Value & Prediction Value
After fitting the model, we can compare the actual values(y_test) with respect to the predicted values & the comparison is shown below:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Actual</th>
      <th>Predicted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.82</td>
      <td>0.807640</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.85</td>
      <td>0.835919</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.52</td>
      <td>0.517341</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.91</td>
      <td>0.915269</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.93</td>
      <td>0.902560</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>70</th>
      <td>0.67</td>
      <td>0.662687</td>
    </tr>
    <tr>
      <th>71</th>
      <td>0.69</td>
      <td>0.672675</td>
    </tr>
    <tr>
      <th>72</th>
      <td>0.66</td>
      <td>0.662211</td>
    </tr>
    <tr>
      <th>73</th>
      <td>0.71</td>
      <td>0.641427</td>
    </tr>
    <tr>
      <th>74</th>
      <td>0.71</td>
      <td>0.728752</td>
    </tr>
  </tbody>
</table>
<p>75 rows × 2 columns</p>
</div>
