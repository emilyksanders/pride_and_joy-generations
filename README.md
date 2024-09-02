# **Pride and Joy, Onward**
This repository is a spinoff of my capstone project from my General Assembly capstone project.  My goal is to improve my processes and develop better models.


# Original Readme Below

# **Pride and Joy**
### *An investigation of mental health correlates in LGBQ+ people*
###### Emily K. Sanders
###### DSB-318, Capstone Project, June 13, 2024
---
###### *A [table of contents](#table-of-contents) for the repository is available at the bottom of this README.*

## Problem Statement
Prior research has established that people with minority sexual identities experience higher rates of psychological distress and mental illness, and that unique factors such as societal oppression and community belonging may serve as deleterious or protective predictors of psychological well-being (for review, see [Sanders & Chalk, 2016](https://cdn.ymaws.com/www.psichi.org/resource/resmgr/journal_2016/Summer16JNSanders.pdf)).  In the current work, I aim to replicate and expand upon these prior findings, so as to better understand the drivers of psychological distress in this population, as well as potential protective factors.  Explicitly, my goal is to create a statistical model from which to draw inferences about different predictive variables.  In my conclusions section, I will interpret these findings and offer suggestions for social, political, and personal actions that we can all take to improve the mental well-being of people with minority sexual identities.

## Terminology
The terminology used for sexual orientations and identities is a perennial source of both discourse and discord.  Although it is always best practice to refer to individuals by the terms they choose for themselves, the practical logistics of a project such as this one, in which many individual's responses are considered in the aggregate, require researchers to choose an umbrella term.  In the original documentation accompanying the dataset I used, the authors referred to their participants as "LGB," which stands for lesbian, gay, and bisexual. However, when reviewing their results, they discovered that many participants identified with terms other than these three (see p. 14-15 of *37166-Documentation-methodology.pdf*, in the download folder with the data).  In order to represent these participants more explicitly, and to avoid the use of acronyms that readers may or may not be familiar with, I opted to use the word "queer" to describe the sample.  Although this term is not preferred by all non-heterosexual or non-cisgender people, it is an established, simple term that is broadly accepted in academia and social movements.  For a brief overview, please see [this excellent guide](https://guides.libraries.indiana.edu/c.php?g=995240&p=8361766) from the Indiana University at Bloomington Library.

## Target Audience
This report is directed primarily at readers with some background knowledge of the topic, although not very much is required.  I have written with the assumption that readers have some basic familiarity with concepts like minority stress, internalized homophobia, and social support, and therefore do not provide extensive definitions or discussions of these ideas and their theoretical backing.  I have, however, attempted to offer brief explanations, that should at least give readers with less prior knowledge an idea of how to search for more information.  I have also written with the assumption that readers have a general understanding of statistical modeling, e.g., linear regression, mean squared error, etc.

## Background and Purpose
Previous research strongly suggests that, in addition to universal stressors like poverty or abuse, unique factors related to social oppression affect the mental health of queer people ([Meyer, 1995](https://www.jstor.org/stable/2137286?origin=crossref)).  Prior research has also found, however, that these same populations can draw on unique sources of strength and protection from psychological harm.  In particular, there is some evidence to suggest that feelings of connection, belonging, and pride in one's sexual minority identity and community may buffer - or even eliminate - the harmful effects of social stigma and oppression ([Fingerhut, Peplau, & Gable, 2010](https://www.tandfonline.com/doi/abs/10.1080/19419899.2010.484592)).  The purpose of the current work is to replicate and expand upon these findings, shedding further light on factors that may promote or hinder the mental wellness of queer people.

## Definition of Success
Because my goal is to create a model for inference, not prediction, I am not overly concerned with its ability to explain all of the variance in the data, nor with its generalizability to other datasets.  I will, of course, attempt to create the best model I can, as measured by $R^2$ and several loss functions.  However, many methods to improve a model's performance (e.g., regularization) impair its interpretability, and would therefore be inappropriate in the current context.  For this reason, I do not expect, and do not require, the exceptional metrics that many of my peers in the field of data science are able to obtain with predictive models.  Instead, I will interpret my results on their own terms, drawing what conclusions I can, relating them to prior findings where possible, and identifying areas that remain ambiguous for followup research.  In this work, the definition of success is simply to understand queer mental health better - even if that understanding is limited to a wish list for future work.

## Deliverables
- A written report of my work and findings, including interpretation and recommendations.  A [table of contents](#table-of-contents) for this report can be found at the bottom of this README.
- A slideshow to accompany the presentation of this report.

## Apparatus
Throughout the course of this project, I used `python` to manipulate, analyze, and model the data. Some of the modules I used include `pandas`, `numpy`, `matplotlib`, `seaborn`, `time`, `datetime`, `os`, `string`, `statsmodels`, and several libraries within `sklearn`. The developers of these modules, and of `python` itself, have graciously made their creations open source. 

## Data
For this investigation, I used a dataset called *Generations*, published by Ilan H. Meyer, Ph.D., in *Data Sharing for Demographic Research* ([DSDR](https://www.icpsr.umich.edu/web/pages/DSDR/index.html)), an archive of data supported by the University of Michigan. Per the terms of the archive, **I have not included the dataset in my public report**. However, the data is publically available and free to access, so any reader wishing to follow along with or replicate my work may do so by following the instructions in the [Introduction](./01_notebooks/01_Introduction_and_Methods.ipynb) notebook. Readers should please note that **none of the notebooks will run unless they first acquire the dataset.**

## Method
Meyer's original study was longitudinal, so the dataset he provided included responses from the participants at up to three different times of measurement, referred to as waves. Due to attrition effects, however, the sample size of participants who responded to all three rounds of data collection was markedly smaller than the original. In the interest of preserving a larger sample, I chose to cross-sectionally investigate the wave 1 responses only, for an initial sample size of 1518. These participants self-identified as queer people (under a variety of terms), but not transgender.  All heterosexual people, and transgender people regardless of orientation, were excluded.  Non-cisgender people who did not identify as transgender (e.g., nonbinary) were included.

Each participant completed the wave 1 questionaire, which included questions on identity, relationships, physical and mental health outcomes and behaviors, and experiences of stress, discrimination, victimization, community, support, and positive identity formation. Many of these questions could be grouped together to form scales.  Where possible, I retained or calculated the scale scores, rather than using individual items.  Meyer and his team completed a great deal of missing value imputation prior to sharing the dataset, and I opted to retain these values.  Where pre-imputed values were not available, I completed my own imputation.  Because of the limited size of the dataset, and the high quality of Meyer's imputation methods, I opted to tolerate a greater proportion of missing data than I otherwise might be inclined to.  I did, however, drop any observations with more than one missing value in the scale comprising the target variable: the Kessler-6 inventory.

Readers are encouraged to review the original documentation that accompanied the dataset for a thorough review of the nature of each variable; in the interest of brevity, I will not include such a review here.  However, I will briefly explain my target variable: participants' scores on the the [Kessler-6 inventory](https://pubmed.ncbi.nlm.nih.gov/12578436/) (Kessler et al., 2003, as cited in the original documentation).  This scale is a general measure of overall mental health, and covers a variety of psychological symptoms and signs of distress.  As explained on p. 22-23 of *37166-Documentation-methodology.pdf*, part of the original documentation:
>\[The Kessler-6 inventory is] a 6-item scale from the National Comorbidity Survey (Kessler et al., 2003). Scale items (w1q77A- w1q77F) asked respondents how often, in the past 30 days, they had felt “nervous,” “hopeless,” “restless or fidgety,” “so depressed that nothing could cheer you up,” “that everything was an effort,” and “worthless.” Responses were recorded on a 5-point scale ranging from “all of the time” to “none of the time.”

The overall score of this scale was calculated by summing up the responses to each item, resulting in scores from 0-24, with higher scores indicating greater mental distress.

Using such a general scale as a target variable allowed me to look for factors that predict overall distress or protection.  Much previous research has used more specific scales to assess specific psychological outcomes, but this approach necessarily requires much more complex interpretation than is feasible for the current project (e.g., in 2016, Sanders and Chalk found that, among gay and lesbian participants, experiencing overt homophobic discrimination predicted many negative outcomes, but internalized homophobia only predicted stress).  Furthermore, using a general scale like Kessler-6 allows researchers to capture distress, even if it manifests differently in different people.  If a suitable model can be found for this variable, the inferences drawn from it may prove to be more generalizable than those related to any one specific psychological symptom(s). 

## Exploratory Data Analysis
After preparing the data, I conducted exploratory data analysis (EDA) to evaluate the different predictors and guide me during the modeling process.  Primarily, this EDA took the form of creating graphs, which can be viewed in the `03_images` folder ([01_main_graphs](../03_images/01_main_graphs) for selected, formatted graphs; [02_all_graphs](../03_images/02_all_graphs) for every graph).  I review the scatterplots of each predictor variable, and took note of those with particularly apparent relationships with the target.

Of particular note, I discovered that the Kessler-6 scores were not normally distributed.  The square roots of these scores adhered better to a normal distribution, but still strayed considerably.  Nonetheless, better is better, and I chose to use the square root of each score as my target variable, rather than the unaltered form.  The implications of this change for the model's interpretability will be discussed below.

I also created a correlation matrix for all remaining features, and reviewed which features were most associated with my target variable (in both forms).  Interestingly, many of the top correlates were general life stressors, rather than queer-specific stressors.  I decided to include examples of both types of stressors in my model, and compare their performance.  If the queer-specific stressors do not improve the performance of the model compared to the general stressors only, it would be a radical departure from the extant literature, requiring serious inquiry and interpretation.  Conversely, if general stressors and queer-specific stressors both contribute to the model's performance, it would reaffirm what other researchers have found: the mental health of queer people is driven by largely the same factors that drive non-queer people's mental health, but is altered and exacerbated by the additional strain or strength conferred on them by their queer identities and communities.

## Modeling
For my first model, I fit a linear regression on features selected more-or-less intuitively.  I selected features that were of interest to me because of my own previous work and experience, as well as those with the most visually striking relationships to the target variable.  These included:

|Queer-Specific Variables|General Variables|Covariates|
|-|-|-|
|connectedness to the queer community|chronic life stress|lifetime suicidality|
|experiences of conversion "therapy" |drug (ab)use       | age|
|perception of anti-queer stigma     |alcohol (ab)use    |income|
|importance of queerness to identity |affiliation with race/ethnic identity|poverty|
|internalized homophobia             |life satisfaction  |US citizenship/residence|
|presence/length of partner relationship|overall happiness|being retired from working|
|outness as a youth|recent mental health| |
|housing discrimination|social support and well-being| |
|interpersonal discrimiation|religiosity| |

This model performed admireably for the subject matter.  $R^2$ was around 0.6 for both training and testing sets, and MSE, RMSE, and MAE were <1 for both sets.  Because the y-variable itself is a square root, this implies that my model is usually within a range of +/-1 with its predictions of the square root of Kessler scores (range: 0-4.9).

## Limitations and Recommendations
The most concerning of the limitations of my work is the age of the dataset.  As mentioned previously, this data is concerned with sensitive personal and political issues, and personal responses are likely to change over time as public opinion fluctuates.  In particular, the current dataset was gathered in 2016, meaning that it pre-dates a great deal of recent political and cultural upheaval, dramatic spikes in public hostility and discrimination towards queer (and many other) people, and a global pandemic with far-reaching, often catastrophic effects.  The resonance of the current results with prior findings offers some encouragement in their utility, but it is imperative to conduct more research on more recent data to establish whether and how any of these effects may have changed in recent history.

Furthermore, the current project was constrained to a tight turn-around schedule, which necessitated many simplifying assumptions and actions.  In particular, in the future, I hope to assess the extent to which the imputation of missing values may have changed the results.  As is common in such long questionaires, many participants exhibited fatigue effects and did not complete all of the questions.  In the Adverse Childhood Experiences scale items in particular, in which a disproportionately high number of responses were missing, it also seems likely that many participants chose not to answer the questions; i.e., these values were not randomly missing, as appears to be the case in most other features.  First Meyer, and then I, imputed all of these values, so as to not sacrifice all the responses the participants did provide.  This is common practice in data science, and indeed most fields that use statistical techniques, but it always carries the risk of introducing error into the dataset.  The wealth of features in this dataset carried a proportionate tax of missing values, leading to large number (if a small percentage) of imputed values in the "cleaned" data I used for modeling.  I would be very interested to see if different approaches to this problem result in substantially different models.  

However, the current work is not without its practical value.  The relatively good performance of this model (for a model of its type, on this topic) offers further evidence for what advocates and experts have been saying for years: queer people's disproportionate rates of psychological distress and mental illness is not a mystery, nor is there any evidence to suggest it is an inherent or immutable part of the identity.  Poor psychological outcomes in this community are driven by how they are supported in society and treated in their communities.  Poverty, stress, and oppression based on who they are as people can drag their mental health down, but support and acceptance from other people, connection to a community of other queer people, and pride and comfort in their identities can build it back up.  If we as a society want to improve the mental health of queer people, we must stop alienating them, and instead offer them the consideration and connection we would offer anyone else.

## Dataset Citation
Meyer, Ilan H. Generations: A Study of the Life and Health of LGB People in a Changing Society, United States, 2016-2019. Inter-university Consortium for Political and Social Research \[distributor\], 2023-01-05. https://doi.org/10.3886/ICPSR37166.v2

## Table of Contents
|Folder|Contents|Description|
|--------|-----------|---------------|
|(none)|readme|This is the current file.|
|(none)|sanders_capstone_pride_and_joy.pdf|The presentation slides that accompany this report.|
|/01_notebooks||This folder contains a collection of Jupyter notebooks, in which readers can find examples of the `python` code I used to process the data and run my analyses, as well as brief written explanations.  These notebooks are named in the order I recommend reading them.  Readers who wish to follow along or replicate my work must proceed through the notebooks in order.|
||01_Introduction_and_Methods.ipynb|An overview of the purpose of the project and methodological strategy.|
||02_Data_Preparation_Part_1.ipynb|Preparing the data for modeling by reducing excess features and imputing missing values.|
||03_Data_Preparation_Part_2.ipynb|Preparing the data for modeling via feature engineering.|
||04_Exploratory_Data_Analysis.ipynb|Investigating the distributions and relationships between variables.|
||05_Modeling.ipynb|Creating my model(s).|
||06_Discussion_and_Conclusions.ipynb|Model interpretation, and consequent discussion of limitations and recommendations.|
||emilys_functions.py|The `python` code of the custom function I used to create graphs for EDA.  It is in a `.py` file so I could import it for use in notebooks.  Readers are welcome to peruse this file, but there is no need.  It exists for technical reasons only.|
||z_Appendix_Function_Definitions.ipynb|The same functions as in the `.py` file, but presented in a notebook for readability.|
|/02_data||This folder is the designated output location for any data files created within the notebooks; however, per the terms of the DSDR archive, I have not included any data files in it with my report.  Instructions for obtaining the data can be found in the *Introduction and Methods* notebook.
||README.md|This is a brief explainer to and placeholder in the `02_data` folder.|
|/03_images||This folder contains images, mostly graphs, that support the report.|
||/01_all_graphs|This folder contains two subfolders, each containing histograms, box plots, qqplots, and scatterplots of all variables, plus two heatmaps.  Readers are welcome to peruse these graphs, but please note that they are provided as supplementary materials only.  They have not been individually formatted, and may be difficult to read.|
||/01_all_graphs/kessler-6|In this subfolder, the scores on the Kessler-6 inventory scores themselves are used as the target variable.  Each other variable is plotted against these scores in a scatterplot, and one of the heatmaps isolates the column of correlations regarding this variable.|
||/01_all_graphs/kessler-6_sqrt|The same plots as above, except the square root of the Kessler-6 inventory scores are used as the target variable.|
||/99_report_images|This folder contains images that are used in the report.|
||/image_output|This is the designated output location for any images (graphs) generated within the notebooks.  Like the `/02_data` folder, I have not included any of my own files in this folder (see the folders above for my images) when submitting the report.  This folder is meant for readers who choose to follow along and reproduce my work, including the generation of plots.|
||/image_output/README.md|This is a brief explainer to and placeholder in the `image_output` folder.|
|LICENSE||The terms by which my work can be accessed and used.|
|.gitignore||Administrative purposes only.|