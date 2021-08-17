# elkhalil_and_fortier_project

BrainHack School 2021 project

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/lilielkhalil">
        <img src="https://avatars.githubusercontent.com/u/87989383?v=4?s=100" width="100px;" alt=""/>
        <br /><sub><b>Lili El Khalil</b></sub>
      </a>
      <br />
    </td>
    <td align="center">
      <a href="https://github.com/eddyfortier">
        <img src="https://avatars.githubusercontent.com/u/72314243?v=4" width="100px;" alt=""/>
        <br /><sub><b>E. Fortier</b></sub>
      </a>
      <br />
    </td>
  </tr>
</table>

## Lili El Khalil's personal Backgroung

Hello !!

My name is Lili El Khalil,
I am in my first year of master student at University of Montreal studying psychology.
I am a research assistant with Marie Audrey Lavoie in the visual neurocognition laboratory.

<b> Why BrainHack School? </B>

When joining the BrainHack School, i was looking farward in particular to know more about data analyses and BIDS validation
Which means to be able to analyse my research data results later on and to know how to validate it with BIDS.

In my research Laboratory i was only working with Matlab and my university courses was only about HTML.
But in BrainHack School i had the opportunity to discover more than one application and method.

You can join me on GitHub at [lilielkhalil](https://github.com/lilielkhalil) or by mail at <lilykhalil98@gmail.com>

## E. Fortier's bio

Mr. Fortier is a Master student in Psychology at Université de Montréal.
Before that, he did a first Bachelor degree in Music writing (B. Mus.) and a second Bachelor degree in Cognitive neuroscience (B. Sc.).
Having backgrounds in both of these fields, his research interests include auditory perception, music perception and creation, and noise pollution's effects on perception and health (physical and mental).
He is currently part of the auditory perception and protection branch of the Projet Courtois NeuroMod (Centre de recherche de l'Institut universitaire de gériatrie de Montréal).

## Project Definition

## Project background

The Projet Courtois NeuroMod is a longitudinal fMRI data acquisition project where participants get scanned almost every week.
One risk associated with intensives protocols like this one is the chronic exposure of the participants to high noise levels during the scan sessions.
This is why it is important to regularly monitor their auditory health to ensure that the research protocol is not causing any damage to the participants' hearing.
Part of the auditory perception's job is to do this monitoring task.
To do so, the participants go through different clinical tests every month to keep track of the evolution of their auditory health.
Some of those test data, such as the pure-tone audiometry test data, are more easily interpreted when rendered into graphic displays.
But with these repeated test comes important amount of data to process.
A first task that could be interesting to do would be, in order to go through the data processing more efficiently, to build an automated pipeline to generate the graphs.

##### Exemple of audiogram

![P01-Baseline 2, Bilateral.png](images/P01-Baseline_2_Bilateral.png)

##### Exemple of Matrix test results graph

![P01-Matrix test FR, Condition 2 (may_2021).png](images/P01-Matrix_test_FR_Condition_2_(may_2021).png)

A second task that could be interesting to do would be to try and use these test data to try and fingerprint the participant based on their results to the tests.
Since every person's hearing is unique and is affected by the individual auditory experience, it could be interesting to try that kind of machine learning classification task.
The third task that could be interesting to do is regarding the dataset formatting.
Since the dataset is not currently BIDS compatible, it could be interesting to create a jupyter notebook to automatically create a BIDS format database from the data.

## Tools

The plan is to use the following tools from the BrainHack School's tutorials in this project:

- Python scripts to execute the graph generation and machine learning tasks
- The Bash terminal environment to work on the python scripts and run them
- Git and GitHub for the collaborative work and the version control of the project
- Plotting libraries such as Matplotlib, Seaborn or Plotly
- Machine learning libraries for the fingerprinting task
- Jupyter Notebook to build and execute the BIDS formatting script
- The BIDS validator to make sure that the formatting worked
- Markdown to build this README.md file

## Data

The dataset used for this project was acquired through multiple sessions with each participant between November 2018 and June 2021.
Multiple clinical tests were performed including:
- Otoscopic inspection of the external auditory canal and tympanic membrane
- Tympanometry
- Stapedial reflex test
- Pure-tone audiometry
    - Regular clinical frequencies range (from 250 Hz to 8 kHz)
    - Ultra-high frequencies extended range (from 9 kHz to 20 kHz)
- Matrix speech-in-noise perception test
    - In the primary language of the participant: French or English (for all participants)
    - In the second language of the participant: French or English (for 5 out of the 6 participants)
- Otoacoustic emissions
    - Transitory evoked otoacoustic emissions (TEOAE)
    - Distortion product otoacoustic emissions (DPOAE) with a L1/L2 ratio of 65/55 dB SPL
    - Growth function (DP Growth) with 2 kHz, 4 kHz and 6 kHz

Baselines were acquired for each of these tests.
Three different combinations of those tests were then designed as experimental conditions and randomly assigned to each of the participant in a way that they will all do each of those conditions four times over the course of a twelve months protocol.

## Deliverables

By the end of The BrainHack School, we aimed to have the following:

- A README.md file to present the project
- A GitHub repository documenting the project
- Python scripts to create graphs and execute machine learning tasks
- Jupyter notebooks with code and explanations for the BIDS formatting task
- A [slideshow](https://docs.google.com/presentation/d/1TveZjzR9TDlGQA-XrLYjqPEb2E-x2vvl0kyfu43ljaQ/edit?usp=sharing) presentation showing the project results
 
## Results

#### Mr. Fortier's progress overview

A first iteration of functional python scripts to generation single test graphs and test overview graphs for each of the Projet Courtois NeuroMod participants is now available in the code folder of this repository.
These scripts were also linted using flake8 and passed all the generic requirements of this linter.

#### Tools and skills that were developped during this project

- **Python scripts**: It was a first attempt to code in python using scripts instead of the Jupyter Notebook controlled environment.
- **Python scripts**: It was also a first attempt at using multiple scripts for a single task and importing functions across them.
- **Git and Github**: This project is the first attempt at building a complete project from the start, using Git's functions and a Github repository.
- **Plot.ly's `graph_objects` tools**: This project was a first on many front regarding Plot.ly.
    - It was a first attempt at doing interactive figures/graphs.
    - It was a first contact with Plot.ly's library.
    - It was a challenge to be able to build graphs that fully represent the particularities of the two different types of figure produced in this project: `plotly.express` might have been easier to use than `plotly.graph_objects`, but it was not as capable to fully build the vision planned for this project.
    - It was an important challenge to navigate in the impressive documentation of the `plotly.graph_objects` library. It is a powerful, extensively customizable tool, but it is also very complex.
- **flake8 linter**: It was the first use of a linter to proof read the scripts' code format.

##### Exemple of interactive HTML audiogram

<div>
  <script type="text/javascript">
    window.PlotlyConfig = {MathJaxConfig: 'local'};
  </script>
  <script src="https://cdn.plot.ly/plotly-2.2.0.min.js">
  </script>
  <div id="1d2bda49-70e2-436d-b970-d633fb3fd192" class="plotly-graph-div" style="height:100%; width:100%;">
  </div>
  <script type="text/javascript">
    window.PLOTLYENV=window.PLOTLYENV || {};
    if (document.getElementById("1d2bda49-70e2-436d-b970-d633fb3fd192")) {
      Plotly.newPlot(    
        "1d2bda49-70e2-436d-b970-d633fb3fd192",    
        [{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"red"},"mode":"lines+markers","name":"Sub01 - PTA, Baseline 1: Baseline (Right Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[0.0,0.0,0.0,10.0,10.0,0.0,10.0,10.0,15.0,5.0,10.0,25.0,30.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"blue"},"mode":"lines+markers","name":"Sub01 - PTA, Baseline 1: Baseline (Left Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000,16000],"y":[0.0,0.0,-5.0,10.0,5.0,5.0,5.0,10.0,0.0,5.0,10.0,15.0,20.0,35.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"red"},"mode":"lines+markers","name":"Sub01 - PTA, Baseline 2: Baseline (Right Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[10.0,10.0,0.0,15.0,10.0,5.0,-5.0,-5.0,15.0,15.0,5.0,25.0,45.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"blue"},"mode":"lines+markers","name":"Sub01 - PTA, Baseline 2: Baseline (Left Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[5.0,5.0,5.0,10.0,5.0,10.0,0.0,-5.0,-5.0,5.0,15.0,20.0,35.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"red"},"mode":"lines+markers","name":"Sub01 - PTA, Month 2: Condition 2 (2-7 days post-scan) (Right Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[10.0,5.0,0.0,15.0,10.0,5.0,0.0,0.0,20.0,10.0,5.0,30.0,60.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"blue"},"mode":"lines+markers","name":"Sub01 - PTA, Month 2: Condition 2 (2-7 days post-scan) (Left Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[5.0,10.0,10.0,5.0,5.0,10.0,5.0,-5.0,-5.0,15.0,20.0,15.0,30.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"red"},"mode":"lines+markers","name":"Sub01 - PTA, Month 3: Condition 2 (2-7 days post-scan) (Right Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[10.0,10.0,0.0,20.0,15.0,10.0,0.0,0.0,15.0,15.0,15.0,30.0,45.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"blue"},"mode":"lines+markers","name":"Sub01 - PTA, Month 3: Condition 2 (2-7 days post-scan) (Left Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[10.0,10.0,5.0,10.0,10.0,10.0,0.0,0.0,10.0,25.0,20.0,20.0,35.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"red"},"mode":"lines+markers","name":"Sub01 - PTA, Month 4: Condition 1A (right before the scan) (Right Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[15.0,15.0,0.0,15.0,15.0,10.0,0.0,0.0,15.0,20.0,10.0,35.0,45.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"blue"},"mode":"lines+markers","name":"Sub01 - PTA, Month 4: Condition 1A (right before the scan) (Left Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[10.0,10.0,15.0,10.0,15.0,15.0,15.0,15.0,-5.0,10.0,15.0,15.0,30.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"red"},"mode":"lines+markers","name":"Sub01 - PTA, Month 4: Condition 1B (right after the scan) (Right Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[10.0,10.0,0.0,20.0,15.0,10.0,0.0,5.0,15.0,15.0,10.0,35.0,50.0]},{"hovertemplate":"%{x:1.0f} Hz<br>%{y:1.0f} dB HL","line":{"color":"blue"},"mode":"lines+markers","name":"Sub01 - PTA, Month 4: Condition 1B (right after the scan) (Left Ear)","type":"scatter","x":[250,500,1000,2000,3000,4000,6000,8000,9000,10000,11200,12500,14000],"y":[10.0,10.0,10.0,15.0,10.0,15.0,5.0,0.0,-5.0,10.0,20.0,15.0,35.0]}],                        {"template":{"data":{"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"choropleth":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"choropleth"}],"contour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"contour"}],"contourcarpet":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"contourcarpet"}],"heatmap":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmap"}],"heatmapgl":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"heatmapgl"}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"histogram2d":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2d"}],"histogram2dcontour":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"histogram2dcontour"}],"mesh3d":[{"colorbar":{"outlinewidth":0,"ticks":""},"type":"mesh3d"}],"parcoords":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"parcoords"}],"pie":[{"automargin":true,"type":"pie"}],"scatter":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter"}],"scatter3d":[{"line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatter3d"}],"scattercarpet":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattercarpet"}],"scattergeo":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergeo"}],"scattergl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattergl"}],"scattermapbox":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scattermapbox"}],"scatterpolar":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolar"}],"scatterpolargl":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterpolargl"}],"scatterternary":[{"marker":{"colorbar":{"outlinewidth":0,"ticks":""}},"type":"scatterternary"}],"surface":[{"colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"type":"surface"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}]},"layout":{"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"autotypenumbers":"strict","coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]],"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]},"colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"geo":{"bgcolor":"white","lakecolor":"white","landcolor":"#E5ECF6","showlakes":true,"showland":true,"subunitcolor":"white"},"hoverlabel":{"align":"left"},"hovermode":"closest","mapbox":{"style":"light"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","gridwidth":2,"linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white"}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"ternary":{"aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"bgcolor":"#E5ECF6","caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"title":{"x":0.05},"xaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2},"yaxis":{"automargin":true,"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","zerolinewidth":2}}},"title":{"text":"Sub01 - Pure-Tone Audiometry"},"xaxis":{"linecolor":"black","range":[2.0,4.301029995663981],"showline":true,"title":{"text":"Frequency (Hz)"},"type":"log"},"yaxis":{"dtick":10,"linecolor":"black","range":[80,-20],"showline":true,"title":{"text":"Hearing Threshold (dB HL)"},"zeroline":true,"zerolinecolor":"black","zerolinewidth":1}},
        {"responsive": true}
      )
    };
  </script>       
</div>

##### Exemple of Matrix test interactive HTML graph

![Sub01-Matrix test FR, All runs](images/Sub-01_MTX_L1_Francais_All_runs.html)
