
import os, random
import nltk
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
import spam as sf
 
def detect_spam(folder, classifier, setting):
    output = {}
    file_list = os.listdir(folder)
    for a_file in file_list:
        f = open(folder + a_file, 'r',encoding='utf-8', errors='ignore')
        features = sf.get_features(f.read(), setting)
        f.close()
        output[a_file] = classifier.classify(features)
    for item in list(output.keys()):
        print (item + '\t' + output.get(item))
 
def print_stat(folder, classifier, setting):
    total = 0
    spam = 0
    ham = 0
    file_list = os.listdir(folder)
    for a_file in file_list:
        total+=1
        f = open(folder + a_file, 'r',encoding='utf-8', errors='ignore')
        features = sf.get_features(f.read(), setting)
        f.close()
        if classifier.classify(features) == 'spam':
            spam+=1
        else:
            ham+=1
    print('%.2f' % (100*float(spam)/float(total)) + '% spam messages')
    print('%.2f' % (100*float(ham)/float(total)) + '% ham messages')
 
def explore_feats(dataset):
    stoplist = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()
    words = []
    for messages in dataset:
        words += [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(messages) if not word.lower() in stoplist]
    #fdist = nltk.FreqDist(words)
    #fdist.plot(75, cumulative=True)
 
if __name__ == "__main__":
    spam = sf.init_lists('enron1/spam/')
    ham = sf.init_lists('enron1/ham/')
    all_messages = [(messages, 'spam') for messages in spam]
    all_messages += [(messages, 'ham') for messages in ham]
 
    spam2 = sf.init_lists('enron2/spam/')
    ham2 = sf.init_lists('enron2/ham/')
    all_messages += [(messages, 'spam') for messages in spam2]
    all_messages += [(messages, 'ham') for messages in ham2]
 
    random.shuffle(all_messages)
    print ('Corpus size = ' + str(len(all_messages)) + ' messages')
 
    all_features = [(sf.get_features(messages, 'bow'), label) for (messages, label) in all_messages]
    train_set, test_set, classifier = sf.train(all_features, 0.8)
 
    sf.evaluate(train_set, test_set, classifier)
 
    #classify your new 
    #run_online(classifier, "")
 
    detect_spam('enron2/ham/', classifier, "")
 
    print('\nHAM:')
    print_stat('enron2/ham/', classifier, "")
    print('SPAM:')
    print_stat('enron2/spam/', classifier, "")
    explore_feats(spam)