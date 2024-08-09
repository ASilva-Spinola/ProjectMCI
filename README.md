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
Tackling the limitations of the field, there are three types of opportunities that can be explore: 
1. Treatment, specifically segmentation into clinical trials; 
2. Monitoring, as maximizing the resources in the clinical setting; 
3. Forecasting, as planning ahead the disease course and moving towards personalized medicine.

For any of these, traditional data analysis methods are not highly accurate since they usually evaluate occurrence, providing results that can lack precision and are time-consuming and costly. Therefore, we need to apply advance techniques that can lead to a robust evaluation of the key factors.
The later can be supervised or unsupervised machine learning (ML) algorithm that aid in the generation of categories and profiles. They are flawed, since they do not generate precise representations over time. But, this issue can be dealt by the use of time-dependent probability models.
The most common ML algorithm used for AD -according to the literature- are: Random Forest, Decision trees, Support Vector Machine, Convolutional Neural Networks, k-Nearest Neighbor. For more information about this, read the article *"The Road to Personalized Medicine in Alzheimer's Disease: The Use of Artificial Intelligence"* [Silva-Spinola et.al 2022 Biomedicines](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8869403/pdf/biomedicines-10-00315.pdf) 

»»Size and quality of the data are key aspects for the application of ML algorithm, if there is an interest of increasing the sample there are several strategies that can be applied, for example: Create more synthetic data based on the one provided or apply for access to sources developed for scientific investigation and teaching like the Alzheimer's Disease Neuroimaging Initiative [ADNI](https://adni.loni.usc.edu/data-samples/access-data/). 
(!) Both of these approaches require attention to the inherent characteristics of the population, external validity and inclusion/exclusion criteria.

As an example, we will apply the :desktop_computer: **Uniform Manifold Approximation and Projection (UMAP)** algorithm for dimension reduction:
UMAP is a graph-based dimensionality reduction technique with two main phases. In the first phase, UMAP constructs a weighted nearest-neighbor graph from the high-dimensional dataset. This graph represents the local structure of the data by capturing the relationships between data points. In the second phase, UMAP computes a low-dimensional representation of the data by optimizing an objective function designed to preserve the essential characteristics of the nearest-neighbor graph. This process aims to maintain the local and global structure of the data in a more interpretable form. [Dadu et al. 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10318357/pdf/main.pdf).
By applying UMAP, we can effectively characterize our dataset [Simulation MCIs Coimbra](https://github.com/ASilva-Spinola/Projects/blob/main/SimulationMCIsCoimbra.csv) and identify potential patterns or structures within it -by assessing the color-coded distribution of the variables-. This method enables us to explore the underlying relationships and variations in our data, providing valuable insights into its structure and aiding in the extraction of meaningful clinical patterns.
To validate the robustness of the identified clusters, we will apply the partition clustering algorithm *K-Means* and evaluate the results using *silhouette scores*. This approach will help us assess the quality and cohesion of the clusters by measuring how well-separated and distinct they are. The *silhouette score* provide an indication of the cluster's internal consistency and how well each data point fits within its assigned cluster compared to others. For a comprehensive understanding of the appropiate use and interpretation of *silhouette scores* in clustering analysis, see the study by [Costa et al. 2023]([https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8869403/pdf/biomedicines-10-00315.pdf](https://pdf.sciencedirectassets.com/272371/1-s2.0-S1532046423X00033/1-s2.0-S1532046423000497/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLWVhc3QtMSJGMEQCIDbLScif6QldcKJhTdOHn5KK7n4d1%2Ba7WGZk1S7ISP%2FRAiBI4f%2Fj76f2CuiA2xTbSSxpXpVXs0OkXqOCI1SeeaV1NiqzBQhHEAUaDDA1OTAwMzU0Njg2NSIMAxBwPvStrWs2F3m0KpAFSIjtD2QqTGKVQZKv4EEg8jWFXwRJITqEvxDqgds3y0lVEINzbLAU%2BdVIzfaNJH0rZvkG5ODvxm9zVvYOOjSL5kiJSvCL%2BY6tC4WURS21SY%2BSzStzlgkYJsPLiVY2BiY9ZfRC%2B0rB35DfUAhCZf9jlhHV8W8pGH2dVhbl95nzzpxU0e7NPXWOq8C54MNOFviWBKKUufKV25fMKSNjBP0DCz%2FFE77kD%2Bdy67XwVdo1OlkTUjnVygfYy16OQ6RQGqot5naW%2FixJJYRfQieqlVQYPsltxFttqHVHOtfnT6yxqVus%2F0qHKxjuHkdDaAXxTaa5ZxxIdNMQsWZzL%2FGzyMs6qtXTjOu1y1x0Y7Hx2jc7dEYh6qeZzx97inbDB9QpsDsUMTT6dYL35BPAj%2F8dQ15pdBhzYOuN%2FZsVnPkbSVx%2FHf5YIQIXhO0kItUsSTr57mTlD2NQzGi0LirGEtqaBI%2F%2FnO5JwLZWrt7ik6DbJBRE%2BrPg1ny7mEEXWD5VlVAluuwEshVlo%2BC38%2FHkgugXuY8LshAy4wBzoqEgUjy0HzlhoJTW%2FV5hg8xCe3rL23Q4mWPmDTeKOIytl9SudsvK9tfs4DWr8zQhIieviZ2OEp1M49uTb5STxG%2FcW8%2F0WSuJ8CJ2qw0feSskmMkLirIukppRoguE4H1%2B6uh3v6OJuu6abRjK04af6PwL0qaStvNqEhw6YIXj8O3pmKnXk%2F%2FR3NtaIh%2BP4Uw10S9%2FCjjkuPOHLwQlAtupLG0kmNsl9937uiUo75s6mpiZ4XSZYub%2Bd5lzaJBK4lhX87m974mmtfbtf0MijNXkxx3eFIbbX%2BIwwbnl%2F61S0TNqsi0MDg59LvoYU4G5RW7WRs5mETOMF08%2BKxIwrLzYtQY6sgHgvkIlRxviuWcmPWSu4O7nGGoiBODPuAr5XUXSFW6s9mzaceb11nWWrvYBuyXj1p4bNFJPYmUimfV70sRnPjDn8nYOHHXyK9%2FOLrSQWDOT4RHZ7oypBsc4%2FSPNKmmhh8L1woNmggsFaJTdqWbcORUQtwm2rsiQHlyfM4VKazZ%2FNMDOAQAukP9S5M55TlZBRFuqIf4OrUyRcs4v8DcesQ7cA2866CIjLYQPUtJ8a%2FCVr0DE&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240809T144715Z&X-Amz-SignedHeaders=host&X-Amz-Expires=299&X-Amz-Credential=ASIAQ3PHCVTYUJI46WP3%2F20240809%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3549536f93edad7d420e7c4aae270ed427baedcb0584b962277ca9c44292a92f&hash=d3e2e7abc64559f3b27200a53537cf9da08ff0aed1fe09f9b3af614b06a45fc6&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1532046423000497&tid=spdf-7d86b2da-c146-4734-bc61-f526ecb758c8&sid=535673669af77742954b092-0a0a73833be8gxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=12125c05575e570650&rr=8b088a524b0c94fe&cc=pt)).     
 
