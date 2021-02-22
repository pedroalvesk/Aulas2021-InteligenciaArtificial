# 2021-02-22
# Inteligencia Artificial - Aula 01 - Agentes
# You need to install: https://github.com/aimacode/aima-python

#
#   Reflex Agent Vacuum
#
from agents4e import ReflexVacuumAgent, TrivialVacuumEnvironment


def test_ReflexVacuumAgent():
    # Observações:
    # Uma vez que não tem memória, quando está tudo limpo o agente anda a saltar de lado para lado.
    print(f"\nAgente ReflexVacuumAgent (nao tem memoria):")

    # create an object of the ReflexVacuumAgent
    agent = ReflexVacuumAgent()
    # create an object of TrivialVacuumEnvironment
    environment = TrivialVacuumEnvironment()
    # add agent to the environment
    environment.add_thing(agent)

    # run the environment
    nPassos = 10    # numero total de passos de simulaçao a executar
    for passo in range(nPassos):
        print_simulation_status(passo, environment, agent)
        environment.step()

    # estado final
    print_simulation_status(nPassos, environment, agent)


#
#   Print simulation status
#
def print_simulation_status(passo, environment, agent):
    print(f"\nEstado Inicial t={passo}:")
    print(f"Perceçao do agente: {environment.percept(agent)}")
    print(f"Estado do ambiente: {environment.status}")


##############################
##          Main            ##
##############################
if __name__ == '__main__':
    test_ReflexVacuumAgent()
