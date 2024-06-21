import h5py

# Adjust the model_path to the correct location of your model file
model_path = '/home/sirjana/Videos/Documents/Django/HTD/HTDapp/models/my_model_epoch_100.h5'

# Open the .h5 model file
with h5py.File(model_path, 'r') as f:
    # Print the keys in the file
    print("Keys:", list(f.keys()))

    # Get the model configuration and print it
    model_config = f.attrs.get('model_config')
    if model_config:
        print("Model config:", model_config.decode('utf-8'))
    else:
        print("No model configuration found.")
