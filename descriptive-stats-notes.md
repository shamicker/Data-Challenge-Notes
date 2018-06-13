# Descriptive Statistics

## Intro to Research Methods (lesson 3)
### Constructs
- In scientific theory, particularly psychology, a hypothetical construct is an explanatory variable which is not directly observable. (itchiness, happiness, stress, intelligence, motivation, etc)

- measured with an **operational definition**.
- For instance, *happiness* could be measured by the ratio of minutes spent smiling to minutes not smiling. Here, the ratio is the **operational definition** of *happiness*.

### Extraneous Factors
- aka lurking variables
- things that could influence the outcome, that aren't necessarily considered. (the surprise unknowns)

### Population Parameter
- denoted by <code>$\mu$</code> (mu)
- are values that describe the ENTIRE population (as an average)

### Sample statistics
- denoted by <code>$\bar{x}$</code> (x-bar)
- are values that describe a sample (the sample that were tested) (as an average)

We use <code>$\bar{x}$</code> to estimate <code>$\mu$</code>.

**Independent** or the **predictor** variable - the x-axis variable

**Dependent** or the **outcome** variable is the y-axis variable

---
### Correlation does not prove causation!

---
### Observational studies
- To show relationships.
- Just ask people and you'll see a trend.

### Surveys
- a type of observational study
- **response bias** - when respondents don't understand a question
- **non-response bias** - when they refuse to answer a question

### Controlled experiment
- to show **causation**
- to deal with all the extraneous factors (lurking variables)

### Within subject design
- controlling for variation within a person.
- For example, testing after different amounts of sleep. You're controlling the variation in people's individual memory capabilities, depending on the amounts of sleep they got.

### Indicator Response
- ex. Pouched rats scratching near tea eggs containing TNT. So I guess it's *indicating* that TNT is nearby. The humans needed some kind of **indicator response** from the mice to know when there was TNT nearby.

---
## Visualizing Data

### Frequency Table
- counts the frequency of each data type (ie, if countries, then each country)
- they are whole numbers, obviously, since it's a count.

### Relative Frequency
- How much of the whole each data point comprises.
- **Absolute** numbers are whole numbers (12 or 43 out of 50)
    - the sum is the number of data points (<code>$n$</code> or <code>$N$</code>)
- **Proportions** are the fraction written with decimals (.24 or .86)
    - the sum is 1
- **Percentages** are with the <code>%</code> sign (24% or 86%)
    - the sum is 100%

### Bar Chart
- measures **frequency** of your data, which is grouped into **intervals** or **bins**
- the **intervals** are on the x-axis
- the **frequency** is on the y-axis

### Bar Graph
- data is grouped **categorically** or **qualitatively**
- can't be grouped (much) differently because the groups are distinct categories
- space between data groupings

### Histogram
- a type of bar chart
- data is grouped **numerically** or **quantitatively**
- *no* space between data groupings (unless frequency is 0)
- the **intersection of the axes** is (0,0) (Cartesian coordinates)
- can be *biased*! Always look at labels & numbers

### InterActivate is a *histogram software*

### Normal distribution
- one large, middle peak called the **mode**; symmetrical

### Positively skewed distribution
- peak is on the left
- most values on the left

---
## Central Tendency

3 measures of center: mode, median, mean

### Mode
- most common occurrence - ie, in [1, 2, 3, 4, 4] it's 4
- value at which the *frequency* is highest (the tallest peak)
- can be used for any data - *categorical* or *numerical*
- no actual formula for finding it.

### Mean
- the **average** of the distribution
- ALL scores in distribution affect the mean
- mean of a sample denoted by <code>$\bar{x}$</code>
- mean of a population denoted by <code>$\mu$</code>
- formula for a sample: <code>$\bar{x} = \frac{\sum x}{n}$</code>
- formula for a population: <code>$\mu = \frac{\sum x}{N}$</code>
- many samples from the same population will have similar means (!!!)
- the mean of a sample can be used to make inferences about the population it came from (!!!)
- **outliers** - outlying data points that completely skew the average
[tough quiz](https://classroom.udacity.com/courses/ud002-bert/lessons/1489118552/concepts/773143370923)

### Median
- value in the middle of the distribution
- if there are 2 numbers, it's the middle of the middles (the average of the middle 2 numbers)
- **ROBUST** = doesn't change much due to outliers
- best measure of central tendencies when dealing with highly skewed distributions
- formula for an even number of values:
<code>$\frac{x_\frac{n}{2} + x_{\frac{n}{2}+1}}{2}$</code>
- formula for an odd number of values: <code>$x_\frac{n+1}{2}$</code>

---
## Variability

### Interquartile Range (IQR)
- divide the data into quarters, and subract the lower median from the upper median (Q3 - Q1). This is the IQR.
- roughly 50% of data is within this range
- IQR is **not affected by outliers**.
- more or less describes the spread of the data

### Outliers
- extreme data points in a distribution
- traditionally cut off top and bottom 25%
- formula to determine outliers: <code>$Outlier < Q_1 - 1.5*(IQR)$</code>
- formula to determine outliers: <code>$Outlier > Q_3 - 1.5*(IQR)$</code>
- traditionally cut off top and bottom 25% of distributions to account for outliers

### Boxplots
- used to visualize *quartiles* and *outliers*
- outer lines are the *min* and *max* values that are NOT outliers
- the whole box is the *IQR*
- the box edges are, as shown in image below, *Q1*, *Q2*, and *Q3*
- *outliers* are shown as dots outside of the *min* and *max* lines.

![boxplot image](images/boxplot.PNG)

![image](images/match-the-boxplots.PNG)

### Deviation (from the *mean*/average)
- find the *mean*, then subtract each data point (find the absolute)
- <code>$x_i - \bar{x}$</code> (xi minus x-bar)
- how far from zero it is

### Squared deviations
- just the *deviations* squared

### SS
- sum of the squared deviations
- formula: <code>$\Sigma(x_i - \bar{x})^2$</code>

### variance
- **SS** divided by <code>$n$</code>
- is the average squared deviation
- BUT if we treated the whole as a sample (<code>$n$</code>), it would be divided by (<code>$n - 1$</code>)
    - I don't know why

### Standard Deviation
- denoted by (small sigma) <code>$\sigma$</code>
- square root of the variance (which is the average of squared deviations)
- the most common measure of spread
- formula: <code>$\sigma=\sqrt{\frac{\Sigma(x_i - \bar{x})^2}{n}}$</code>
- within a *normal distribution*, 68% of data sample falls within a 'standard deviation' from the mean, and 95% of the data sample falls within 2 'standard deviations' from the mean (see figure!).

![point of standard deviation](images/point-of-standard-deviation.PNG)

### Bessel's Correction
In general, samples under-estimate variability in a population because samples tend to be from the middle (especially in normal distribution).
- To correct for this, *Bessel's Correction*
- get average using <code>$(n-1)$</code> instead of <code>$n$</code>
- use this **ONLY** for approximating populations using samples
- it is **NOT** used for a whole population (or small data set)
- if you've got a sample, where <code>$n = 5$</code> and population is <code>$N = 100$</code>, then use Bessel's Correction.
- denoted by (small s) <code>$s$</code>

**Sample standard deviation** is the standard deviation of a sample (not a population), and it uses *Bessel's Correction* to approximate the population. Its formula is: <code>$s \approx \sqrt{\frac{\Sigma(x_i - \bar{x})^2}{n-1}}$</code>

Variance with Bessel's Correction (for a sample): <code>$\frac{\Sigma(x_i = \bar{x})^2}{n-1}$</code>

---
## Standardizing

### Standardizing
This term is used to compare 2 different distributions (ie Twitter vs Facebook followers). Basically, we compare them using their standard deviations as the common unit. For example, we would compare how many standard deviations away from the mean (which is our zero starting point) that our Z-value is.
- proportion below or above the mean

### Continuous Distribution
A theoretical model:
- a theoretically continuous (smooth) distribution that can be described with an equation, which calculates the proportion between ANY 2 points on the x-axis.
- area under the curve should be 1 (same as the sum of all the relative frequencies)

In our theoretical model of a *continuous* and *normal* distribution, the *mean*, *median*, and *mode* are all equal.

### Z
- Marks a point on the x-axis of a distribution
- The number of standard deviations away from the mean

If we want to calculate this Z in terms of standard deviations from the mean,
we need to know:
- the Z number
- the mean
- the standard deviation
And then take the difference (mean minus Z) divided by the stand.dev.

### Z-Score
- in a standard distribution, the distance in st.dev's away from mean (0).
- <code>$Z = \frac{x-\mu}{\sigma}$</code> where <code>$x - \mu$</code> will be positive or negative, depending on whether above or below the *mean*.

### Standard Normal Distribution
Q: What is the standard deviation of a standardized distribution?

A: The z-score of sigma will be 1:

<code>$Z = \frac{x - \mu}{\sigma} = \frac{\sigma - 0}{\sigma} = 1$</code>

This is called the **Standard Normal Distribution**.

![pic of Standard Normal Distribution](images/standard-normal-distribution.PNG)

---
## Normal Distribution

### Normal Distribution
- bell curve with peak in the center
- the tails never actually touch the x-axis, they just infinitely approach it
    - because we can never be 100% sure that there isn't a value further than that; theoretically, you can have an infinite values in a population


### Probability Density Function (PDF)
- the curve of a *normal distribution*
- because the area under the curve is 1
    - so we can get the probability of any number on x-axis (aka %)
- there is an extra-curricular equation for this (via calculus)
    - someone created a table for greater ease!
- the *area under the curve* of a normal distribution == the *probability* of randomly selecting less than x == the *proportion* in the sample/population with scores less than x
    - where x is the xth percentile (or the Z)


<code>$s \approx \sqrt{\frac{\Sigma(x_i - \bar{x})^2}{n-1}}$</code>

<code>$Zscore = \frac{\mu -Z}{\sigma}$</code>, and then look up the *area under the curve* on the chart to get the *probability* of data scores less than *X* (or *Z*)

---
## Sampling Distributions

### Central Limit Theorem
- the distribution of means, where every mean is the mean of a sample of size <code>$n$</code>, has a standard deviation equal to the population standard deviation divided by the square root of <code>$n$</code>.
- for any population, if you take enough samples, and plot those samples' means, you'll get roughly a normal distribution
- aka the *standard error(SE)*


## Standard Error (SE)
- the standard deviation of the sampling distribution
- the population standard deviation divided by the square root of n:

<code>$SE = \frac{\sigma}{\sqrt{n}}$</code>

![central limit theorem notes](images/central-limit-theorem-notes.PNG)
