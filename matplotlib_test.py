#!/usr/bin/python
# -*- coding:utf8 -*- 为了支持中文注释
import matplotlib.pyplot as plt
import numpy as np

class ShowChart:
    def showBarChart(self,y_pos, performance, error, people):
        np.random.seed(19680801)
        plt.rcdefaults()
        fig, ax = plt.subplots()
        ax.barh(y_pos, performance, xerr=error, align='center',
                color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Send Message Count')
        ax.set_title('Who do you talk to most ?')

        plt.show()
if __name__ == '__main__':
    # Fixing random state for reproducibility


    # plt.rcdefaults()
    # fig, ax = plt.subplots()

    # Example data
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    # ax.barh(y_pos, performance, xerr=error, align='center',
    #         color='green', ecolor='black')
    # ax.set_yticks(y_pos)
    # ax.set_yticklabels(people)
    # ax.invert_yaxis()  # labels read top-to-bottom
    # ax.set_xlabel('Performance')
    # ax.set_title('How fast do you want to go today?')
    #
    # plt.show()
    chart = ShowChart()
    chart.showBarChart(y_pos, performance, error, people)

