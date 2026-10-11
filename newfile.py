{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "932ff45b-596d-449e-a118-49d465fbef32",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d4e44d8a-06a7-4b7a-8ea3-09adb59e2bbc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c9aae07a-35c0-4281-9acd-1696a9b1ecf2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(np.random.rand(20,5),np.arange(20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "273eda28-67f4-4897-bbc0-7f6f6e9817cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.605403</td>\n",
       "      <td>0.504750</td>\n",
       "      <td>0.062690</td>\n",
       "      <td>0.115598</td>\n",
       "      <td>0.670653</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.735386</td>\n",
       "      <td>0.852033</td>\n",
       "      <td>0.879409</td>\n",
       "      <td>0.091987</td>\n",
       "      <td>0.953454</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.974076</td>\n",
       "      <td>0.297112</td>\n",
       "      <td>0.769674</td>\n",
       "      <td>0.582923</td>\n",
       "      <td>0.693397</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.325571</td>\n",
       "      <td>0.684929</td>\n",
       "      <td>0.961006</td>\n",
       "      <td>0.469838</td>\n",
       "      <td>0.412149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.825737</td>\n",
       "      <td>0.086641</td>\n",
       "      <td>0.583027</td>\n",
       "      <td>0.113595</td>\n",
       "      <td>0.278012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0.451848</td>\n",
       "      <td>0.170101</td>\n",
       "      <td>0.921961</td>\n",
       "      <td>0.568536</td>\n",
       "      <td>0.047231</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>0.267830</td>\n",
       "      <td>0.120250</td>\n",
       "      <td>0.262720</td>\n",
       "      <td>0.121419</td>\n",
       "      <td>0.886196</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>0.781766</td>\n",
       "      <td>0.056116</td>\n",
       "      <td>0.107292</td>\n",
       "      <td>0.435115</td>\n",
       "      <td>0.406506</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>0.669415</td>\n",
       "      <td>0.145158</td>\n",
       "      <td>0.634220</td>\n",
       "      <td>0.447040</td>\n",
       "      <td>0.333797</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>0.043503</td>\n",
       "      <td>0.235117</td>\n",
       "      <td>0.025456</td>\n",
       "      <td>0.946325</td>\n",
       "      <td>0.060719</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>0.239468</td>\n",
       "      <td>0.955213</td>\n",
       "      <td>0.506233</td>\n",
       "      <td>0.400938</td>\n",
       "      <td>0.152713</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>0.313916</td>\n",
       "      <td>0.843472</td>\n",
       "      <td>0.723975</td>\n",
       "      <td>0.745303</td>\n",
       "      <td>0.606728</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>0.111800</td>\n",
       "      <td>0.573044</td>\n",
       "      <td>0.704978</td>\n",
       "      <td>0.913157</td>\n",
       "      <td>0.221709</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>0.023608</td>\n",
       "      <td>0.561494</td>\n",
       "      <td>0.702055</td>\n",
       "      <td>0.134202</td>\n",
       "      <td>0.963160</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>0.093939</td>\n",
       "      <td>0.776429</td>\n",
       "      <td>0.903828</td>\n",
       "      <td>0.600265</td>\n",
       "      <td>0.273853</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>0.921507</td>\n",
       "      <td>0.538498</td>\n",
       "      <td>0.734191</td>\n",
       "      <td>0.308000</td>\n",
       "      <td>0.261722</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>0.865760</td>\n",
       "      <td>0.228302</td>\n",
       "      <td>0.763539</td>\n",
       "      <td>0.094714</td>\n",
       "      <td>0.798290</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>0.827974</td>\n",
       "      <td>0.312700</td>\n",
       "      <td>0.430998</td>\n",
       "      <td>0.269358</td>\n",
       "      <td>0.555111</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>0.125252</td>\n",
       "      <td>0.336000</td>\n",
       "      <td>0.668750</td>\n",
       "      <td>0.273874</td>\n",
       "      <td>0.770954</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>0.344527</td>\n",
       "      <td>0.189612</td>\n",
       "      <td>0.918488</td>\n",
       "      <td>0.096659</td>\n",
       "      <td>0.351027</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           0         1         2         3         4\n",
       "0   0.605403  0.504750  0.062690  0.115598  0.670653\n",
       "1   0.735386  0.852033  0.879409  0.091987  0.953454\n",
       "2   0.974076  0.297112  0.769674  0.582923  0.693397\n",
       "3   0.325571  0.684929  0.961006  0.469838  0.412149\n",
       "4   0.825737  0.086641  0.583027  0.113595  0.278012\n",
       "5   0.451848  0.170101  0.921961  0.568536  0.047231\n",
       "6   0.267830  0.120250  0.262720  0.121419  0.886196\n",
       "7   0.781766  0.056116  0.107292  0.435115  0.406506\n",
       "8   0.669415  0.145158  0.634220  0.447040  0.333797\n",
       "9   0.043503  0.235117  0.025456  0.946325  0.060719\n",
       "10  0.239468  0.955213  0.506233  0.400938  0.152713\n",
       "11  0.313916  0.843472  0.723975  0.745303  0.606728\n",
       "12  0.111800  0.573044  0.704978  0.913157  0.221709\n",
       "13  0.023608  0.561494  0.702055  0.134202  0.963160\n",
       "14  0.093939  0.776429  0.903828  0.600265  0.273853\n",
       "15  0.921507  0.538498  0.734191  0.308000  0.261722\n",
       "16  0.865760  0.228302  0.763539  0.094714  0.798290\n",
       "17  0.827974  0.312700  0.430998  0.269358  0.555111\n",
       "18  0.125252  0.336000  0.668750  0.273874  0.770954\n",
       "19  0.344527  0.189612  0.918488  0.096659  0.351027"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dad395f3-c63e-4ce9-90c7-6a6fdd7cae83",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(20, 5)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a530f9ba-8b8b-4ebe-b2e5-b5defe41ad57",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.000000</td>\n",
       "      <td>20.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.477414</td>\n",
       "      <td>0.423349</td>\n",
       "      <td>0.613225</td>\n",
       "      <td>0.386442</td>\n",
       "      <td>0.484869</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.325977</td>\n",
       "      <td>0.284990</td>\n",
       "      <td>0.293034</td>\n",
       "      <td>0.273414</td>\n",
       "      <td>0.292678</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.023608</td>\n",
       "      <td>0.056116</td>\n",
       "      <td>0.025456</td>\n",
       "      <td>0.091987</td>\n",
       "      <td>0.047231</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.210914</td>\n",
       "      <td>0.184734</td>\n",
       "      <td>0.487424</td>\n",
       "      <td>0.119964</td>\n",
       "      <td>0.270820</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.398187</td>\n",
       "      <td>0.324350</td>\n",
       "      <td>0.703517</td>\n",
       "      <td>0.354469</td>\n",
       "      <td>0.409327</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.792759</td>\n",
       "      <td>0.601016</td>\n",
       "      <td>0.797108</td>\n",
       "      <td>0.572133</td>\n",
       "      <td>0.712787</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>0.974076</td>\n",
       "      <td>0.955213</td>\n",
       "      <td>0.961006</td>\n",
       "      <td>0.946325</td>\n",
       "      <td>0.963160</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               0          1          2          3          4\n",
       "count  20.000000  20.000000  20.000000  20.000000  20.000000\n",
       "mean    0.477414   0.423349   0.613225   0.386442   0.484869\n",
       "std     0.325977   0.284990   0.293034   0.273414   0.292678\n",
       "min     0.023608   0.056116   0.025456   0.091987   0.047231\n",
       "25%     0.210914   0.184734   0.487424   0.119964   0.270820\n",
       "50%     0.398187   0.324350   0.703517   0.354469   0.409327\n",
       "75%     0.792759   0.601016   0.797108   0.572133   0.712787\n",
       "max     0.974076   0.955213   0.961006   0.946325   0.963160"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "455affc8-3361-43a5-b3a3-d0b94bdadc94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 20 entries, 0 to 19\n",
      "Data columns (total 5 columns):\n",
      " #   Column  Non-Null Count  Dtype  \n",
      "---  ------  --------------  -----  \n",
      " 0   0       20 non-null     float64\n",
      " 1   1       20 non-null     float64\n",
      " 2   2       20 non-null     float64\n",
      " 3   3       20 non-null     float64\n",
      " 4   4       20 non-null     float64\n",
      "dtypes: float64(5)\n",
      "memory usage: 960.0 bytes\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "db6f128f-2e7b-4d87-945e-415d849179c8",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'DataFrame' object has no attribute 're_index'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_18595/336678506.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mre_index\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/.local/lib/python3.10/site-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, name)\u001b[0m\n\u001b[1;32m   6202\u001b[0m         ):\n\u001b[1;32m   6203\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 6204\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mobject\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__getattribute__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   6205\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   6206\u001b[0m     \u001b[0;34m@\u001b[0m\u001b[0mfinal\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'DataFrame' object has no attribute 're_index'"
     ]
    }
   ],
   "source": [
    "df.re_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74b27c79-5761-416c-9288-3081e207ab60",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.DataFrame(list(\"abcde\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8db9d782-d4f7-4c0d-bc7e-01f9babeea62",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.rename(columns = pd.Series(list(\"abcde\")),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d3b4079-c6b1-4158-bcec-de45814673a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74d71a7f-16a1-49a2-833c-e67d85bc2fdb",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.loc[[2,5,7,9,0],[\"c\",\"d\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3477bbe5-f936-4df0-9f93-6a18df07a4a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.iloc[:,[1,2]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d27e71d6-f4e3-4ea9-bcb4-3f3f919005a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb19d2ad-2a30-4dbd-ae6e-f2e8a796c927",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.loc[[0],[\"a\"]]=np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e638597-b1cb-4f31-83f0-36c798c0d417",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "762b2c7d-f0a8-4602-9aa9-00a7113d1f77",
   "metadata": {},
   "outputs": [],
   "source": [
    "df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9571765d-2e7c-4410-873e-4ee47f96a6d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.dropna(subset=[\"a\"],axis=0,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "69adaa53-d36c-400e-92ad-8414d0ddaada",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd776a42-1c1f-4433-a332-abfd493f4f21",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.reset_index(drop=True,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba038e02-b85c-4005-8c5c-ef045891df10",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5fbe2e55-fc68-4fd0-9206-8db5ea3ced13",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.iloc[[7],[4]]=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0376e86c-ee4d-4ebe-a296-b92b055b5b9b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "459f40e1-d9b3-4a74-8fa0-044acb26902c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"e\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38716695-d232-466a-924e-7a74cb09d0ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[df[\"e\"]==1].loc[:,[\"d\",\"e\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3205853e-b9a0-4422-ba0e-2668e9a1e68b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop_duplicates(keep=\"last\",subset=[\"e\"],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "771b6a2f-b7e1-47c4-88f1-58ac101fbc52",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e70bce33-1f60-4f41-a816-c8988536283a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85cf2686-1614-47ac-be0d-d92e31c3ec54",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.reset_index(drop=True,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33091b5a-4dff-4c7e-b036-8566e9fd7ab5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ac3fea3-cabf-4b92-8364-11033ffd2433",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "409b5de0-62e0-4064-bc26-d5f9a7cc9773",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e374d252-7bd8-451b-aed2-9c782c9c3369",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "df.plot(kind=\"line\",x=\"a\",y=\"b\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "324354d5-2188-45a2-a38f-12e512823629",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: matplotlib in /home/surya/.local/lib/python3.10/site-packages (3.8.0)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in /home/surya/.local/lib/python3.10/site-packages (from matplotlib) (1.1.1)\n",
      "Requirement already satisfied: cycler>=0.10 in /usr/lib/python3/dist-packages (from matplotlib) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /usr/lib/python3/dist-packages (from matplotlib) (4.29.1)\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/lib/python3/dist-packages (from matplotlib) (1.3.2)\n",
      "Requirement already satisfied: numpy<2,>=1.21 in /home/surya/.local/lib/python3.10/site-packages (from matplotlib) (1.26.1)\n",
      "Requirement already satisfied: packaging>=20.0 in /usr/lib/python3/dist-packages (from matplotlib) (21.3)\n",
      "Requirement already satisfied: pillow>=6.2.0 in /usr/lib/python3/dist-packages (from matplotlib) (9.0.1)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in /usr/lib/python3/dist-packages (from matplotlib) (2.4.7)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in /home/surya/.local/lib/python3.10/site-packages (from matplotlib) (2.8.2)\n",
      "Requirement already satisfied: six>=1.5 in /usr/lib/python3/dist-packages (from python-dateutil>=2.7->matplotlib) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e32ad55c-e53e-4178-964d-789bcb14e71d",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'matplotlib.pyplot'; 'matplotlib' is not a package",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_20569/1014320233.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpyplot\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m~/Documents/python files/matplotlib.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpyplot\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mmatplotlib\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mstyle\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mstyle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muse\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"dark_background\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscatter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m8\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mlabel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"first\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"my plot\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'matplotlib.pyplot'; 'matplotlib' is not a package"
     ]
    }
   ],
   "source": [
    "import matplotlib.pyplot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c1eeb398-26c8-47cc-bd6e-c492237b863f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pip in /home/surya/.local/lib/python3.10/site-packages (23.3.1)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install --upgrade pip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bfa1d986-b1c2-4493-be11-bfdaf2211834",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'matplotlib.pyplot'; 'matplotlib' is not a package",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_20611/524771496.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mget_ipython\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrun_line_magic\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'matplotlib'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m''\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/usr/lib/python3/dist-packages/IPython/core/interactiveshell.py\u001b[0m in \u001b[0;36mrun_line_magic\u001b[0;34m(self, magic_name, line, _stack_depth)\u001b[0m\n\u001b[1;32m   2362\u001b[0m                 \u001b[0mkwargs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'local_ns'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_local_scope\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstack_depth\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2363\u001b[0m             \u001b[0;32mwith\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbuiltin_trap\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2364\u001b[0;31m                 \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2365\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2366\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<decorator-gen-101>\u001b[0m in \u001b[0;36mmatplotlib\u001b[0;34m(self, line)\u001b[0m\n",
      "\u001b[0;32m/usr/lib/python3/dist-packages/IPython/core/magic.py\u001b[0m in \u001b[0;36m<lambda>\u001b[0;34m(f, *a, **k)\u001b[0m\n\u001b[1;32m    185\u001b[0m     \u001b[0;31m# but it's overkill for just that one bit of state.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    186\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mmagic_deco\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 187\u001b[0;31m         \u001b[0mcall\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mlambda\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mk\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mk\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    188\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    189\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mcallable\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/lib/python3/dist-packages/IPython/core/magics/pylab.py\u001b[0m in \u001b[0;36mmatplotlib\u001b[0;34m(self, line)\u001b[0m\n\u001b[1;32m     97\u001b[0m             \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Available matplotlib backends: %s\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0mbackends_list\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     98\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 99\u001b[0;31m             \u001b[0mgui\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbackend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshell\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0menable_matplotlib\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgui\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgui\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0margs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgui\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    100\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_show_matplotlib_backend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgui\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbackend\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    101\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/lib/python3/dist-packages/IPython/core/interactiveshell.py\u001b[0m in \u001b[0;36menable_matplotlib\u001b[0;34m(self, gui)\u001b[0m\n\u001b[1;32m   3531\u001b[0m         \"\"\"\n\u001b[1;32m   3532\u001b[0m         \u001b[0;32mfrom\u001b[0m \u001b[0mIPython\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcore\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpylabtools\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpt\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3533\u001b[0;31m         \u001b[0;32mfrom\u001b[0m \u001b[0mmatplotlib_inline\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbackend_inline\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mconfigure_inline_support\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3534\u001b[0m         \u001b[0mgui\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbackend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_gui_and_backend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mgui\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpylab_gui_select\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3535\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/lib/python3/dist-packages/matplotlib_inline/backend_inline.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;31m# Distributed under the terms of the BSD 3-Clause License.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m from matplotlib.backends.backend_agg import (  # noqa\n\u001b[1;32m      8\u001b[0m     \u001b[0mnew_figure_manager\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/Documents/python files/matplotlib.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpyplot\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mmatplotlib\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mstyle\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mstyle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muse\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"dark_background\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscatter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m8\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m4\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mlabel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"first\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"my plot\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'matplotlib.pyplot'; 'matplotlib' is not a package"
     ]
    }
   ],
   "source": [
    "matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "46179b8a-5af1-48de-8ffe-ace3cb9c35bb",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3294770864.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_19539/3294770864.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    pip3 install matplotlib\u001b[0m\n\u001b[0m         ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "pip3 install matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "2dc87184-a564-435b-b031-57821a38f1d2",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1943560176.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/tmp/ipykernel_19539/1943560176.py\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    python3 -m pip install matplotlib\u001b[0m\n\u001b[0m               ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "python3 -m pip install matplotlib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ac01b7a-d125-4231-b294-8ebd5edec1ef",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d5e96ba-28de-4523-9843-06f6f61cc963",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
