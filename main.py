import pickle

from q_learning import train_DT_RL, train_RL_RL, train_RL_DT, play_DT_RL, play_RL_DT
from decision_tree import DecisionTree

if __name__ == "__main__":
    ai = DecisionTree()
    ai.train()

    train_RL_DT(ai)


# if __name__ == "__main__":
#     with open('checkpoints/decision_tree.pkl', 'rb') as f:
#         ai = pickle.load(f)

#     with open('checkpoints/q_table_DT.pkl', 'rb') as f:
#         Q = pickle.load(f)

#     play_DT_RL(Q, 100, ai)


