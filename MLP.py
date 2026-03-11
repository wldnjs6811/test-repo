{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4c5dd097-0702-4389-9529-711ace083172",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "device: cpu\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n",
    "print(\"device:\", device)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfa678dc-289e-493c-bf51-fba2969ccc53",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
