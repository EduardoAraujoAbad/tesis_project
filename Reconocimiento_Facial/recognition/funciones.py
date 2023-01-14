import datetime
from users.models import Horarios, Asignacion
from tkinter import messagebox
import time
from datetime import timedelta

# variables to set time


# validate entry entry time of user


def validate_time_entry(user):

    entry = False
    now = datetime.datetime.now()
    timer_now = now.strftime('%H:%M:%S')
    print(timer_now)
    schedule = Horarios.objects.all().filter(user=user.id)

    for value_entry in schedule:

        for asignation in value_entry.horas_asignadas.all():

            asignation_entry = asignation.hora_inicio.strftime('%H:%M:%S')
            # Parse str to a time object
            asignation_entry_obj = datetime.datetime.strptime(
                asignation_entry, '%H:%M:%S')
            # operand with time
            asignation_entry_extra = (
                asignation_entry_obj + timedelta(minutes=10)).strftime('%H:%M:%S')

            if (timer_now >= asignation_entry and timer_now <= asignation_entry_extra):
                entry = True

    return entry

# validate exit time of user


def validate_time_exit(user):

    exit = False
    now = datetime.datetime.now()
    timer_now = now.strftime('%H:%M:%S')
    print(timer_now)
    schedule = Horarios.objects.all().filter(user=user.id)

    for value_entry in schedule:

        for asignation in value_entry.horas_asignadas.all():

            asignation_exit = asignation.hora_fin.strftime('%H:%M:%S')

            # Parse str to a time object
            asignation_exit_obj = datetime.datetime.strptime(
                asignation_exit, '%H:%M:%S')
            # operand with time
            asignation_exit_extra = (
                asignation_exit_obj + timedelta(minutes=10)).strftime('%H:%M:%S')
            print(asignation_exit_extra)

            if (timer_now >= asignation_exit and timer_now <= asignation_exit_extra):
                exit = True

    return exit
