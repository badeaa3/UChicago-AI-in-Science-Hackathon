#!/usr/bin/bash
#SBATCH --account=pi-dfreedman
#SBATCH -p schmidt-gpu
#SBATCH --gres=gpu:1
#SBATCH --qos=schmidt
#SBATCH --time 2:00:00



echo "output of the visible GPU environment"
nvidia-smi

# Use hackathon enviroment
source /project/dfreedman/badea/hackathon/bin/activate

echo JAX
python example_jax.py
echo PyTorch
python example_torch.py
echo Tensorflow
python example_tf.py
