{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39ecf6bb-a9b7-4334-87ed-e9cbaa95d0f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def to_float(value):\n",
    "    try:\n",
    "        return float(value)\n",
    "    except:\n",
    "        return None\n",
    "\n",
    "def clean(value):\n",
    "    return value.strip().lower()\n",
    "\n",
    "test = [\"  123.45 \", \"Invalid\", \"-99\", \"   \", \"Data\"]\n",
    "results = []\n",
    "\n",
    "for item in test:\n",
    "    a = to_float(item)\n",
    "    b = clean(item)\n",
    "    results.append((item, a, b))\n",
    "\n",
    "results"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
