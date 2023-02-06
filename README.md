# Predictive modelling for Alzheimer's disease

The simulated dataset [Simulation MCIs Coimbra](https://github.com/ASilva-Spinola/Projects/blob/main/SimulationMCIsCoimbra.csv) is a fictional representation based on the data from the project titled: **"Application of a computational biomarker-based model to predict progression to Alzheimer's disease"** by PhD candidate for the Faculty of Medicine, University of Coimbra **_Anuschka Silva-Spinola_** in collaboration at the Center for Innovative Biomedicine and Biotechnology (CIBB) and Centre for Informatics and Systems (CISUC).

#### Summary:
Dementia is a major health issue among older people with more than 47.5 million globally, with a serious impact on families, health-care systems, and society. **_Alzheimer's disease (AD)_** represents more than 60% of dementia cases, therefore looking for effective treatments stands as an imperative challenge. Current focus relies on therapies that target the early-stage, **_mild cognitive impairment (MCI)_**, preventing or delaying progression to dementia. With an expanding cohort of elderlies with multiple comorbidities, the complexity of achieving a correct diagnosis and predictive approaches rises. To handle the growing amount of information, **_machine learning_** strategies provide an excellent tool in Dementia Clinics by improving classification, processing large amounts of information, lowering costs, and predicting outcomes. Acknowledging these necessities, **_we aim to develop a biomarker-based model to predict progression in the AD-spectrum_**, optimized for the Portuguese population and to apply it in the clinical-setting to evaluate longitudinal performance.    

#### :brain:The disease:
Alzheimer's disease (AD) is the most common neurodegenerative disorder worldwide, with a prevalence of 3.9% of individuals over the age of 60. The main risk factor is increasing age and 95% of its representation is sporadic -without genetic mutation associated-, therefore it is highly affected by comorbidities and has no effective treatment. For more information see the resources available on the [Alzheimer's association](https://www.alz.org/alzheimers-dementia/what-is-alzheimers) site.

AD is a progressive disease, where dementia symptoms worsen gradually over a period of time. On average, it can take from 4 to 8 years to the onset of the disease and 20 or more on its course. This progression goes to several well-characterized stages referred as the AD-continuum (*Porsteinsson et al. 2021 J Prev Alz Dis*). <p align="center"> <img src="https://www.jpreventionalzheimer.com/wp-content/uploads/2021/05/FIG-1-KNOX.gif" width="750" height="450"> </p> 

The main biological changes associated to AD are characterized by the accumulation of amyloid-beta (AB) plaques and tau-related neurofibrillary tangles (NFT) that affect the prefrontal and mesial-temporal areas of the brain -mainly the hippocampus- and leads to neurodegeneration -atrophy-, as seen in the following image (*Breijyeh & Karaman 2020 Molecules*):<p align="center"> <img src="https://www.mdpi.com/molecules/molecules-25-05789/article_deploy/html/images/molecules-25-05789-g001.png" width="750" height="450"> </p>

This AD neuropathological signature of AB plaques, NFT and neurodegeneration, can be detected by quantifying specific proteins (AB42, AB40, t-Tau, p-Tau181 and NfL) in cerebrospinal fluid (CSF) and peripheral blood -serum/plasma-. This CSF signature can be represented as the AT(N) biomarker grouping following the [2018 NIA-AA Research Framework](https://alz-journals.onlinelibrary.wiley.com/doi/epdf/10.1016/j.jalz.2018.02.018).

#### :clipboard:The dataset:
[Simulation MCIs Coimbra](https://github.com/ASilva-Spinola/Projects/blob/main/SimulationMCIsCoimbra.csv) has 564 individuals -a subset with longitudinal data-. These are classified according to their *diagnosis* (DX) according to their total score on the Clinical Dementia Rating (CDR) as: neurological controls (NC), amnesic MCI (EMCI), non-amnesic MCI (LMCI) and AD.
| DX at screening (total CDR score)  | Sample size, n|
| ---------------- | ------------- |
| NC (0) | 29  |
| EMCI (0.5) | 389  |
| LMCI (0.5) | 87 |
| AD (≥1) | 59  |

As variables -columns- the dataset' content relates to clinical,  demographic, neuropsychological, fluid biomarkers, neuroimaging and genetic information, as follows:

| Clinical | Fluid Biomarkers | Neuropsychological tests | 
| -------- | ----------- | ------------------------ | 
| CONV: Conversion from MCI to AD | CSFNFL: CSF Neurofilament light chain, pg/mL  | MMSE: Mini-Mental State Examination |
| RID: No ID | pNFL: serum NfL, pg/mL | MMMSE.bl: MMSE at baseline |
| DX: Diagnosis | pPTAU181: plasma p-Tau181, pg/mL| MOCA: Montreal Cognitive Assessment |
| MONTH/YEAR: Time of consultation | pAB4240: plasma AB42/AB40 ratio | DIGITSP: Digit span |
| FM: Family history | AB40: CSF 40 amino acid form of amyloid beta, pg/mL | TMTA: Trail Making Test Part A |
| MHPSYCH: Presence of neuropsychiatric disease | AB42: CSF 42 amino acid form of amyloid beta, pg/mL | TMTB: Trail Making Test Part B |
| MHCARD: Presence of cardiovascular disease | AB4240: CSF AB42/AB40 ratio | LMI: Immediate Logic Memory from Wechsler Memory Scale |
| MHRESP: Presence of respiratory disease | TAU: CSF total Tau protein, pg/mL | LMD: Delayed Logic Memory from Wechsler Memory Scale |
| MHHEPAT: Presence of hepatic disease | PTAU: CSF phosphorylated Tau protein at position 181, pg/mL | CDRGLOBAL: Clinical Dementia Rating total |
| MHGAST: Presence of gastric/intestinal disease | AMYLOID: Cutoff of 0.068 CSF AB42/AB40 ratio | CDRSB: CDR Sum-of-boxes |
| MHRENA: Presence of renal/urinary disease | TAUTOPA: Cutoff of 37 pg/mL CSF p-Tau181 | GDTOTAL: Geriatric Depression Scale total |
| MHSTROKE: History of stroke | NEURODEG: Cutoff of 250 pg/mL CSF t-Tau | NPITOTAL: Neuropsychiatric Inventory total |
| MHHYPERT: Presence of hypertension | ATN: AT(N) biomarker grouping | *and their Z-scores obtained according to Normative Portuguese data = named Z.xx* |
| MHALC/MHSMOK: Alcoholism/Smoking | | |

| Neuroimaging | Demographic | Genetic |
| ---------------- | ------------ | ------- |
| CVD: Cerebrovascular disease | AGE: Age, years | APOE4: No of Apolipoprotein (ApoE) E4 |
| LDA: Limbic-predominant atrophy  | EDUCAT: Years of formal education | APGEN1: ApoE allele 1 |
| HSA: Hippocampal atrophy | GENDER: Sex, Male/Female | APGEN2: ApoE allele 2 |
| MA: Generic atrophy | | |
| HIPPOC: Hippocampal volume | | | 
| ENTOR: Entorhinal cortex volume | | |

#### :bar_chart:The models:
Tackling the limitations of the field, there are 3 types of opportunities that can be explore: 
1. Treatment, specifically segmentation into clinical trials; 
2. Monitoring, as maximizing the resources in the clinical setting; 
3. Forecasting, as planning ahead the disease course and moving towards personalized medicine.

For any of these, traditional data analysis methods are not highly accurate since they usually evaluate occurrence, providing results that can lack precision and are time-consuming and costly. Therefore, we need to apply advance techniques that can lead to a robust evaluation of the key factors.
The later can be supervised or unsupervised machine learning (ML) algorithm that aid in the generation of categories and profiles. They are flawed, since they do not generate precise representations over time. But, this issue can be dealt by the use of time-dependent probability models.
The most common ML algorithm used for AD -according to the literature- are: Random Forest, Decision trees, Support Vector Machine, Convolutional Neural Networks, k-Nearest Neighbor. For more information about this, read the article *"The Road to Personalized Medicine in Alzheimer's Disease: The Use of Artificial Intelligence"* [Silva-Spinola et.al 2022 Biomedicines](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8869403/pdf/biomedicines-10-00315.pdf) 

»»Size and quality of the data are key aspects for the application of ML algorithm, if there is an interest of increasing the sample there are several strategies that can be applied, for example: Create more synthetic data based on the one provided or apply for access to sources developed for scientific investigation and teaching like the Alzheimer's Disease Neuroimaging Initiative [ADNI](https://adni.loni.usc.edu/data-samples/access-data/). 
:warning:Both of these approaches require attention to the inherent characteristics of the population, external validity and inclusion/exclusion criteria.
