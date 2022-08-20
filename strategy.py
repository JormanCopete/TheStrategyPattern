import string
import random
from typing import List
from abc import ABC, abstractmethod

def generar_id(length=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class TicketDeSoporte:
    def __init__(self, cliente, problema):
        self.id = generar_id()
        self.cliente = cliente
        self.problema = problema

class EstrategiaDeOrdenamientoTicket(ABC):
    @abstractmethod
    def crear_orden(self, list: List[TicketDeSoporte]) -> List[TicketDeSoporte]:
        pass

class FIFOEstrategiaDeOrdenamiento(EstrategiaDeOrdenamientoTicket):
    def crear_orden(self, list: List[TicketDeSoporte]) -> List[TicketDeSoporte]:
        return list.copy()

class FILOEstrategiaDeOrdenamiento(EstrategiaDeOrdenamientoTicket):
    def crear_orden(self, list: List[TicketDeSoporte]) -> List[TicketDeSoporte]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy

class RandomEstrategiaDeOrdenamiento(EstrategiaDeOrdenamientoTicket):
    def crear_orden(self, list: List[TicketDeSoporte]) -> List[TicketDeSoporte]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy

class BlackHoleStrategy(EstrategiaDeOrdenamientoTicket):
    def crear_orden(self, list: List[TicketDeSoporte]) -> List[TicketDeSoporte]:
        return []

class AtencionAlCliente:
    def __init__(self, processing_strategy: EstrategiaDeOrdenamientoTicket):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def crear_ticket(self, cliente, problema):
        self.tickets.append(TicketDeSoporte(cliente, problema))

    def process_tickets(self):
        ticket_list = self.processing_strategy.crear_orden(self.tickets)

        if len(ticket_list) == 0:
            print("No hay casos para procesar. Todo al día")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: TicketDeSoporte):
        print("==================================")
        print(f"Procesando el ticket No: {ticket.id}")
        print(f"Cliente: {ticket.cliente}")
        print(f"Problema: {ticket.problema}")
        print("==================================")


app = AtencionAlCliente(RandomEstrategiaDeOrdenamiento())

app.crear_ticket("John Smith", "My computer makes strange sounds!")
app.crear_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.crear_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

app.process_tickets()