# Text-to-Image-Generation-using-Stable-Diffusion-1.5-on-Google-Cloud-Platform-Vertex-AI

## Table of Contents

  1. Executive Summary
  2. Introduction
  3. Development Tools and Technologies
  4. Development Tools and Technologies
  5. Google Cloud Platform Vertex AI
  6. Stable Diffusion 1.5 Model
  7. Application Features
  8. Command-Line Interface
  9. Stable Diffusion 1.5 Integration
  10. ControlNets and Self-Attention Guidance
  11. Image Saving and Output
  12. Requirements
  13. Installation
  14. Conclusion
  15. Acknowledgments
  16. References

Done by:
Yashwanth Balan Arumugam
yashwanthbalan75@gmail.com

### 1. Executive Summary
#### Introduction
This report details the development of a command-line interface (CLI) application for text-to-image generation using Stable Diffusion 1.5 on the Google Cloud Platform (GCP) Vertex AI. The application, executed by Yashwanth Balan Arumugam, meets specific requirements outlined by Team Vermillio.

#### Development Tools and Technologies
Google Cloud Platform Vertex AI
GCP Vertex AI was chosen for its scalability and powerful machine learning capabilities, offering access to pre-trained models and simplified deployment of custom solutions.

####Stable Diffusion 1.5 Model
The project utilizes the Stable Diffusion 1.5 model, a cutting-edge machine learning model for text-to-image generation available through the diffusers package.

#### Application Features
Command-Line Interface
The CLI application provides a user-friendly interface with a simple command structure. Users invoke the application using the generate command and provide essential parameters.

#### Stable Diffusion 1.5 Integration
The application seamlessly integrates the Stable Diffusion 1.5 model, renowned for its image generation capabilities, efficiently operating on GCP Vertex AI.

#### ControlNets and Self-Attention Guidance
Advanced features include ControlNets options (Canny, HED, MiDaS, OpenPose) and Self-Attention Guidance (SAG) for enhanced image generation and higher-quality outputs.

#### Image Saving and Output
Generated images are saved to specified file paths and returned as output for user access and utilization.

### 2. Requirements
Installation as an Executable: The application should be installable as an executable and invoked using the generate command.
Stable Diffusion 1.5 Model: The application utilizes the Stable Diffusion 1.5 model for text-to-image generation.
Input Parameters: Text prompt, optional seed, batch size, optional path to an image on disk, type of ControlNet, flag to enable/disable a new artistic style, SAG scale.
Image Generation: The application performs text-to-image diffusion based on the provided information.
Image Saving: Generated images are saved to disk, and their file locations are returned.
ControlNets: The application utilizes Self-Attention Guidance (SAG) along with two ControlNets (Canny, HED, MiDaS, OpenPose).

### 3. Installation
The application is packaged for easy installation using pip. Install it with the following command:

###bash
pip install .


### 4. Conclusion
The CLI application for text-to-image generation on GCP Vertex AI has been successfully developed, meeting Team Vermillio's requirements. It showcases the potential of cloud-based machine learning solutions in image generation tasks.

### 5. Acknowledgments
Gratitude to Team Vermillio, including Ryan McHale and Drew Boshardy, for their guidance throughout the development process.

### 6. References
•	Stable Diffusion model: Link
•	Google Cloud Platform Vertex AI: Link
•	ControlNets: Documentation
•	Self-Attention Guidance: Paper
•	Rafid Siddiqui, J. (n.d.). Personalized-diffusion: A Tutorial on Customized Image Generation by Fine-Tuning the Stable Diffusion Models.
•	Rafid Siddiqui, J. (2022, October 17). Beyond diffusion: What is personalized Image Generation and how can you customize image synthesis? Azad Academy. https://azadacademy.substack.com/p/beyond-diffusion-what-is-personalized 
•	runwayml/stable-diffusion-v1-5 · Hugging Face. (n.d.). Huggingface.Co. Retrieved September 6, 2023, from https://huggingface.co/runwayml/stable-diffusion-v1-5 
•	Stable-diffusion: Latent Text-to-Image Diffusion. (n.d.).
•	TroubleChute [@TroubleChute]. (2022, October 21). v1.5 Download Guide | Stable Diffusion | AUTOMATIC1111’s Web UI. Youtube. https://www.youtube.com/watch?v=sN1r2L8Gg9A 


## Demo:
### CLI Application using stable-diffusion 1.5
#### Command to execute
Once installed, the application can be invoked using the generate command. Example usage:

#### bash
generate --prompt "A fantasy landscape, trending on artstation" --seed 123 --batch_size 1 --image_path /home/yashwanthbalan75/generated_image.jpg --control_net canny --use_style --sag_scale 0.5
Output:

The generated output is organized in the "output_images" directory. The generated image file is named 'generated_image.png.' Use SSH to download the image conveniently.

#### bash
generate --prompt "A man is fishing during a tsunami" --seed 123 --batch_size 1 --image_path /home/yashwanthbalan75/generated_image.jpg --control_net canny --use_style --sag_scale 0.5
Output:

The generated output is stored in the "output_images" directory, and the image file is named 'generated_image.png.' Download the image using SSH.
