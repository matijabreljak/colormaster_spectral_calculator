Since I do not care about readme files the only part of this program written by AI is the readme file itself
This program is completly free od AI, I do not like to use AI for personal projects

# ColorMaster Alpha 1.0 - Spectral Analysis Tool

A Jupyter Notebook-based spectral analysis tool for simulating color rendition through optical filters and film characteristics. ColorMaster allows you to analyze how different optical elements affect color reproduction and exposure in imaging systems.

## Author
**Matija Breljak**

## Overview

ColorMaster simulates the interaction between light sources(not implemented yet, the only lightsoure avaliable is uniform lighting), optical filters, and film/sensor spectral sensitivities. This interactive notebook processes spectral data to calculate RGB color values, exposure changes, and color shifts when applying various optical elements to an imaging pipeline.

## Features

- Spectral Pipeline Processing: Apply multiple optical filters sequentially to simulate real-world optical systems
- Color Calculation: Convert spectral data to RGB color values with white balance correction
- Exposure Analysis: Calculate exposure loss when adding filters to the optical path
- Spectrum Visualization: Plot spectral sensitivity curves using matplotlib
- White Balance Correction: Average-based white balance correction method(may not be optimal for noise in real world)
- Interactive Selection: Choose films, filters, and test samples from CSV databases via input prompts
- Terminal Color Output: Display RGB color swatches directly in the notebook output

## Requirements

- Python 3.x
- Jupyter Notebook or JupyterLab
- NumPy
- Pandas
- Matplotlib
- Colorist (custom RGB color module)

## Usage

1. Launch Jupyter Notebook:
jupyter notebook

2. Open colormaster.ipynb (or your notebook filename)

3. Run the cells sequentially:
   - The first cells will import libraries and load CSV data
   - Follow the interactive input prompts to:
     - Select a film/sensor profile from the numbered list
     - Add optical elements/filters to the pipeline (enter -1 when done)
     - Select a test sample for analysis

4. The notebook will output:
   - Spectral plots showing sensitivity curves at each pipeline stage
   - Color swatches with RGB values for:
     - True white (film only)
     - White through filters
     - Sample color at various pipeline stages
   - Exposure loss calculations(using average)

## Data Format

### CSV Structure
All film spectral data files follow the same format with six columns:
- xc - Wavelength values for Red channel
- yc - Sensitivity values for Red channel (log10 scale for films)
- xm - Wavelength values for Green channel
- ym - Sensitivity values for Green channel (log10 scale for films)
- xy - Wavelength values for Blue channel
- yy - Sensitivity values for Blue channel (log10 scale for films)

### Example CSV Files

Film-List.csv:
index,filename
1,Film_Kodak_Portra400.csv
2,Film_Fuji_Provia100.csv

Element_List.csv:
index,filename
1,Filter-CC-40.csv
2,Filter-KB-12.csv

Sample-List.csv:
index,filename
1,Sample-Leaf.csv
2,Sample_Macbeth_Green.csv

## Pipeline Processing Flow

1. Input: Light source spectrum (uniform assumption) + Sample spectrum
2. Optical Pipeline: Sequential filter application (Spectrum to Filter 1 to Filter 2 to ... to Filter N)
3. Film Response: Modified spectrum multiplied by Film RGB sensitivities
4. Integration: Numerical integration over wavelengths
5. White Balance: Average-based correction
6. Output: RGB values and Exposure loss

## Methods

### Current Implementation (Alpha 1.0)
- White Balance: Average method (scales channels to equal integrated response)
- Lighting: Uniform spectrum assumption
- Integration: Trapezoidal numerical integration
- Interpolation: Linear interpolation for filter application

### Planned Features
- Median and log-based white balance correction
- Non-uniform lighting spectra support
- Black body radiation based light spectrum calculation
- Channel-specific exposure loss analysis
- Batch processing mode
- Export functionality for results

## Notebook Structure

The notebook is organized into these sections:

1. Imports and Setup: Library imports and CSV data loading
2. Function Definitions: Core processing functions
3. Interactive Pipeline Building: User selection of components
4. Processing Pipeline: Main computation and analysis
5. Visualization: Spectral plots and color output
6. Results Display: RGB values, exposure calculations, and color swatches

## Key Functions

- IntegrateChannel() - Numerical integration using trapezoidal rule
- CalculateColorRGB() - Spectral to RGB conversion with white balance
- ApplyFilter() - Multiplicative filter application with interpolation
- ApplyPipeline() - Sequential filter processing
- FilterFilm() - Full pipeline on all three color channels
- CorrectSpectrumAVG() - Average white balance correction
- CalculateExposureLoss() - Log2 exposure difference calculation
- pack() - Recombines separate channel data into DataFrame format

## Terminal Color Output

The notebook uses ANSI escape codes via the Colorist module to display approximate RGB colors in the output. The color swatch represents calculated RGB values.

Note: Terminal color reproduction is limited and serves as a quick visual reference only.

## Limitations

- Alpha version with single white balance method
- Assumes uniform illumination spectrum
- Interactive input mode only (no batch processing)
- Terminal-based color visualization (limited accuracy)
- Manual CSV file management required

## Troubleshooting

### Common Issues

"Colorist module not found"
- Ensure the Colorist module is in your Python path or the same directory as the notebook

"CSV file not found"
- Verify all three CSV list files exist in the working directory
- Check that referenced spectral data files exist

"Index out of range"
- Ensure you're entering valid numbers from the displayed lists
- Remember to enter -1 to stop adding filters

## Contributing

Contributions are welcome! Areas for improvement include:
- Additional white balance methods (median, log, etc.)
- Light source spectrum support
- GUI or widget-based interface
- Export to common color formats (CIE XYZ, Lab, etc.)
- Batch processing capabilities
- Improved inline color visualization

## License

In the license file

## Acknowledgments

This tool was developed for spectral analysis of optical systems and color reproduction simulation in imaging applications.

## Contact

Matija Breljak - contact me via instagram

---
ColorMaster Alpha 1.0 - Jupyter Notebook Spectral Analysis Tool
