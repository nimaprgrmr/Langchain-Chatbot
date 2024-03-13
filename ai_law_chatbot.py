{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "57bd4b59",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter your question: قراردادهاي خصوصي نسبت به كساني كه آنرا منعقد نموده ان\n",
      "قراردادهاي خصوصي نسبت به كساني كه آنرا منعقد نموده ان\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Number of requested results 4 is greater than number of elements in index 2, updating n_results = 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " در صورتي كه مخالف صريح قانون نباشد نافذ است.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "# import sys\n",
    "from langchain.document_loaders import TextLoader\n",
    "from langchain.document_loaders import DirectoryLoader\n",
    "from langchain.indexes import VectorstoreIndexCreator\n",
    "from langchain.llms import OpenAI\n",
    "from langchain.chat_models import ChatOpenAI\n",
    "\n",
    "APIKEY = \"nkfjd-dkfnew2o478320"\n",
    "os.environ['OPENAI_API_KEY'] = APIKEY\n",
    "\n",
    "query = input('enter your question: ')\n",
    "print(query)\n",
    "\n",
    "#loader = TextLoader('data.txt')\n",
    "loader = DirectoryLoader('.', glob='*.txt')\n",
    "index = VectorstoreIndexCreator().from_loaders([loader])\n",
    "\n",
    "print(index.query(query))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6843694a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#print(index.query(query), llm=ChatOpenAI()) baraye tarkibe openai va txt khodeman\n",
    "#llm=ChatOpenAI()"
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
