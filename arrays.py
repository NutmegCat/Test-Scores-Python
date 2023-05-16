class Arrays:
    # initialize variables
    score = 0
    markScores = []
    PRECISION = 10.0
    totalOccurrences = 0

    @staticmethod
    def expand_array(array):
        new_capacity = len(array) * 2
        new_array = [0] * new_capacity
        for i in range(len(array)):
            new_array[i] = array[i]
        return new_array

    @staticmethod
    def main():
        # initial array capacity
        INITIAL_CAPACITY = 11

        # initial array
        markScores = [0] * INITIAL_CAPACITY
        totalOccurrences = 0

        # ask for scores
        while True:
            score = int(input("\nEnter a score (or a negative value to exit): "))

            # exit loop
            if score < 0:
                break

            # ignore values over 11
            if score < INITIAL_CAPACITY:
                # Expand the scores array if it gets full
                if totalOccurrences == len(markScores):
                    markScores = Arrays.expand_array(markScores)

                markScores[score] += 1
                totalOccurrences += 1

        # print table headers
        print("\nScore\t\t# of Occurrences")

        # calculate average
        sum = 0.0
        mean = 0.0
        for i in range(len(markScores)):
            if markScores[i] != 0:
                print(f"{i}\t\t{markScores[i]}")
                sum += i * markScores[i]

        mean = sum / totalOccurrences

        # print average
        print("\nMean score:", round(mean * Arrays.PRECISION) / Arrays.PRECISION)


# Call the main function
Arrays.main()
