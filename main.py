from tkinter import *
from tkinter import ttk, filedialog
import tkinter.messagebox
import subprocess
import itertools
import os
import datetime
import webbrowser
from collections import defaultdict
try:
    import mysql.connector
    import pandas
    from tkcalendar import *
    import matplotlib.pyplot as plt
    import numpy as np
    import phonenumbers
except ModuleNotFoundError:
    data_ = subprocess.call(['pip', 'install', 'mysql-connector'])
    data__ = subprocess.call(['pip', 'install', 'pandas'])
    data___ = subprocess.call(['pip', 'install', 'tkcalendar'])
    data____ = subprocess.call(['pip', 'install', 'matplotlib'])
    data_____ = subprocess.call(['pip', 'install', 'numpy'])
    data______ = subprocess.call(['pip', 'install', 'phonenumbers'])
    import mysql.connector
    import pandas
    from tkcalendar import *
    import matplotlib.pyplot as plt
    import numpy as np
    import phonenumbers


class KhataBook:
    def __init__(self):
        self.root = root
        self.root.title("Khata book")
        self.root.geometry("800x600+160-90")
        """______________________________________variables______________________________________________"""
        add_name = StringVar()
        add_address = StringVar()
        add_phone = StringVar()
        add_amount = StringVar()
        add_date = StringVar()
        del_name = StringVar()
        update_name = StringVar()
        search = StringVar()
        host = 'localhost'
        user = 'root'
        password = 'blc332'
        plus_amt = StringVar()
        minus_amt = StringVar()
        # current working directory
        cur = os.curdir
        # date time
        now = datetime.datetime.now()
        cur_year = now.year
        cur_month = now.month
        cur_day = now.day
        months = {'01': 'Jan', '02': 'Feb', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                  '07': 'July', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

        month_int = ['0', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']  # ignore 0
        # _______________checking if database exists or need to be created______________________
        connection_ = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor_ = connection_.cursor()
        select_command_ = "SHOW databases"
        cursor_.execute(select_command_)
        record_tuple_ = cursor_.fetchall()
        record_list2 = list(itertools.chain(*record_tuple_))
        if "khatabook_records" in record_list2:
            pass
        else:
            cursor_.execute("CREATE DATABASE Khatabook_records")
        database = "Khatabook_records"

        # creating a table in database IF NOT EXISTS
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = connection.cursor()
        table_command = "CREATE TABLE IF NOT EXISTS records(name varchar(255) NOT NULL,address varchar(255) NOT NULL," \
                        "phone varchar(200) PRIMARY KEY ,amount int NOT NULL ,date varchar(200))"
        cursor.execute(table_command)
        bd_table_command = "CREATE TABLE IF NOT EXISTS bad_debts(name varchar(255),address varchar(255)," \
                           "phone varchar(200),amount int,date varchar(200))"
        cursor.execute(bd_table_command)

        """_______________________________________functions_________________________"""
        # def check_phone_number(phone_number, region):
        #     num = phonenumbers.parse(phone_number, region)
        #     phonenumbers.is_valid_number(num)

        def au(_event=None):
            global screen1
            screen1 = Toplevel(root)
            screen1.title("Information About Developer")
            screen1.geometry("400x380")
            colo = 'white'
            screen1.configure(bg=colo)

            def git():
                webbrowser.open('https://github.com/vanshugalhotra3332')

            def instagram():
                webbrowser.open('https://instagram.com/vanshu_galhotra')

            lbl1 = Label(screen1, text="Developed by :- Vanshu Galhotra ", font=('helvetica', 15, 'bold'),
                         bd=7, bg='white')
            lbl1.grid(row=0, column=0)
            lbl2 = Label(screen1, text="Email:- vanshugalhotra3332@gmail.com", font=('helvetica', 15, 'bold'),
                         bd=7, bg='white')
            lbl2.grid(row=1, column=0)
            lbl3 = Button(screen1, text="Instagram :-  vanshu_galhotra", font=('helvetica', 17, 'bold'), bd=7,
                          bg='white', overrelief=RIDGE, command=instagram)
            lbl3.grid(row=2, column=0)
            lblg = Button(screen1, text="Github:- vanshugalhotra3332", font=('helvetica', 17, 'bold'), bd=7,
                          bg='white', overrelief=RIDGE, command=git)
            lblg.grid(row=3, column=0)
            lble = Label(screen1, text="", font=('helvetica', 7, 'bold'), bd=2,
                         bg=colo)
            lble.grid(row=4, column=0)
            lbl_v = Label(screen1, text="© Copyright : Vanshu Galhotra", font=('helvetica', 9, 'bold'),
                          bd=2, bg=colo)
            lbl_v.grid(row=5, column=0)
            btne = Button(screen1, padx=18, bd=7, font=('helvetica', 16, 'bold'), width=7, text="Exit",
                          bg='gold2', overrelief=RIDGE, command=lambda screen=screen1: exit_system(screen))
            btne.grid(row=6, column=0)
            lblp = Label(screen1, text="Coded in python", font=('helvetica', 9, 'bold'),
                         bd=2, bg=colo)
            lblp.grid(row=7, column=0)

        def git_repo():
            webbrowser.open('https://github.com/vanshugalhotra3332/khatabook')

        def date_amount_formatting():
            select_command1 = "SELECT amount, date FROM records"
            cursor.execute(select_command1)
            record_tuple11 = cursor.fetchall()
            num_list = list(itertools.chain(*record_tuple11))
            connection.commit()

            keys_ = num_list[0:len(num_list)+1:2]   # fetching keys for dict using slicing(every odd value)
            values_ = num_list[1:len(num_list)+1:2]  # fetching values for dict using slicing(every even value)
            global num_dict
            num_dict = defaultdict(list)
            # creation of dictionary like this {'2020-05-15': [5000], '2020-12-28': [2000, 10000]}
            for value, key in zip(keys_, values_):
                num_dict[key].append(value)

            final_dict_ = dict(num_dict)
            global dict_we_want   # will use it to create ts graph
            dict_we_want = {key: sum(values) for key, values in final_dict_.items()}  # sum up all values of same key
            list_of_time = list(dict_we_want.keys())
            global sorted_time
            sorted_time = sorted(list_of_time, key=lambda g: datetime.datetime.strptime(g, "%Y-%m-%d")
                                 .strftime("%Y-%m-%d"))  # sorts time in ascending order

            #  _____________converting sorted time to alphabet months like 2020-12-03 will be 3 dec 2020___________
            year_list = []  # creating empty lists to store loop variable values later on.
            global month_list
            month_list = []
            day_list = []

            # to ensure month_list only includes month entries of current year
            index_emp = []
            sorted_time_cur_only = []
            for index_cur in range(0, len(sorted_time)):    # appending index at which year is current year
                if sorted_time[index_cur].startswith(str(cur_year)):
                    index_emp.append(index_cur)

            for index_cur_ in index_emp:    # appending all current year entries here
                sorted_time_cur_only.append(sorted_time[index_cur_])

            for y in sorted_time:    # storing all years from sorted time to year_list
                year_list.append(y[0:4])    # using slicing and nothing else

            for m in sorted_time_cur_only:    # storing all months from sorted time to year_list
                month_list.append(m[5:7])    # using slicing and nothing else

            for d in sorted_time:    # storing all days from sorted time to year_list
                day_list.append(d[8:])    # using slicing and nothing else

            month_list_alpha = []     # will store months like dec, nov etc. here
            for month in month_list:    # converting number months to there alpha character like 11 to nov
                month_list_alpha.append(months[month])   # using months dictionary for this declared above

            global day_month_list_alpha  # gonna use it outside the function
            day_month_list_alpha = []   # here we gonna store day+month like 3 dec
            # this is list which contains 2 separate lists of days and months_alpha
            day_month_list = [day_list] + [month_list_alpha]  # like [ ['day1', 'day2'], ['mon1','mon2'] ]
            for index in range(0, len(day_month_list[0])):
                # index will include values from 0 to len(['day1','day2'])that is 2
                # now put value of day_month_list[0] and index to understand following.
                # day_month_list means ['day1', 'day2'] and index will be 0 at first loop
                # so day_month_list[0][index] is day1 which is concatenated with day_month_list[1][index] or mon1
                # which results day1 mon1 and then appended to day_month_list_alpha list
                day_month_list_alpha.append(day_month_list[0][index] + '' + day_month_list[1][index])

            # now we gonna concatenate day_month_alpha with year like 30nov 2020
            dmy_list = []  # creating empty list to store values later on
            # creating list of 2 lists that is day_month_alpha created above and year list
            dm_y_list = [day_month_list_alpha] + [year_list]
            for index_ in range(0, len(dm_y_list[0])):
                dmy_list.append(dm_y_list[0][index_] + ' ' + dm_y_list[1][index_])

        def show_ts_ls():  # last 7 days
            """Plotting time series graph"""
            date_amount_formatting()  # calling the function to use its globalized values
            x = np.array(day_month_list_alpha[-7:])  # getting last 7 values from sorted time format like 28 dec
            list_of_val = []   # empty list to store values of last 7 days
            for items_st in sorted_time[-7:]:    # getting last 7 values from sorted time format like '2020-12-28'
                list_of_val.append(dict_we_want[items_st])
            y = np.array(list_of_val)

            plt.plot(x, y, '--')
            plt.xlabel('Days')
            plt.ylabel('Amount')
            plt.title('Credit Of Last 7 Days')
            plt.show()

        def show_ts_lm():   # last month
            date_amount_formatting()  # calling the function to use its globalized values
            list_of_indexes = []  # empty list to store values of indexes at which we got current month date
            current_month_list = []  # empty list to store current month dates using above list
            for indexes in range(0, len(month_list)):  # range function to get indexes at which we got current month
                if month_list[indexes] == str(cur_month):   # if statement to assure that index we got is of cur month
                    list_of_indexes.append(indexes)   # appending indexes to a list to use it further

            for cur_index in list_of_indexes:    # passing every index from above list to get the dates accordingly
                current_month_list.append(day_month_list_alpha[cur_index])  # creating a list of all dates of cur month
            current_month_list_ = []   # this will include items from sorted time

            # this is for dict values which we gonna use to create y array
            for cur_index_ in list_of_indexes:
                current_month_list_.append(sorted_time[cur_index_])

            values_for_dict = []
            for items_ in current_month_list_:
                values_for_dict.append(dict_we_want[items_])
            final_dict_ = dict(zip(current_month_list_, values_for_dict))

            """Plotting time series graph"""
            x = np.array(current_month_list)
            y = np.array(list(final_dict_.values()))
            if len(x) > 1:
                plt.plot(x, y)
                plt.xlabel('Days')
                plt.ylabel('Amount')
                plt.title('Credit During This Month')
                plt.show()
            else:
                plt.plot(x, y, 'x')   # separate treatment for entries less than 1
                plt.xlabel('Days')
                plt.ylabel('Amount')
                plt.title('Credit During This Month')
                plt.show()

        def amount_for_particular_month(month_in_int):
            date_amount_formatting()
            list_of_indexes1 = []
            pm_month_list = []
            for indexes in range(0, len(month_list)):
                if month_list[indexes] == month_int[month_in_int]:
                    list_of_indexes1.append(indexes)

            for cur_index in list_of_indexes1:
                pm_month_list.append(day_month_list_alpha[cur_index])

            pm_month_list_ = []
            # this is for dict values which we gonna use to create y array
            for cur_index_ in list_of_indexes1:
                pm_month_list_.append(sorted_time[cur_index_])

            values_for_dict = []
            for items_ in pm_month_list_:
                values_for_dict.append(dict_we_want[items_])
            global final_dict_1
            final_dict_1 = dict(zip(pm_month_list_, values_for_dict))
            return final_dict_1

        def pie_m():
            date_amount_formatting()
            """Now we have to get all month's date like we did above for just cur month"""
            # _______________________________________for january
            amount_for_particular_month(1)
            dict_of_values_for_jan = final_dict_1
            total_amount_jan = sum(list(dict_of_values_for_jan.values()))
            # _______________________________________for february
            amount_for_particular_month(2)
            dict_of_values_for_feb = final_dict_1
            total_amount_feb = sum(list(dict_of_values_for_feb.values()))
            # _______________________________________for march
            amount_for_particular_month(3)
            dict_of_values_for_march = final_dict_1
            total_amount_march = sum(list(dict_of_values_for_march.values()))
            # _______________________________________for april
            amount_for_particular_month(4)
            dict_of_values_for_april = final_dict_1
            total_amount_april = sum(list(dict_of_values_for_april.values()))
            # _______________________________________for may
            amount_for_particular_month(5)
            dict_of_values_for_may = final_dict_1
            total_amount_may = sum(list(dict_of_values_for_may.values()))
            # _______________________________________for june
            amount_for_particular_month(6)
            dict_of_values_for_june = final_dict_1
            total_amount_june = sum(list(dict_of_values_for_june.values()))
            # _______________________________________for july
            amount_for_particular_month(7)
            dict_of_values_for_july = final_dict_1
            total_amount_july = sum(list(dict_of_values_for_july.values()))
            # _______________________________________for august
            amount_for_particular_month(8)
            dict_of_values_for_aug = final_dict_1
            total_amount_aug = sum(list(dict_of_values_for_aug.values()))
            # _______________________________________for september
            amount_for_particular_month(9)
            dict_of_values_for_sep = final_dict_1
            total_amount_sep = sum(list(dict_of_values_for_sep.values()))
            # _______________________________________for october
            amount_for_particular_month(10)
            dict_of_values_for_oct = final_dict_1
            total_amount_oct = sum(list(dict_of_values_for_oct.values()))
            # _______________________________________for november
            amount_for_particular_month(11)
            dict_of_values_for_nov = final_dict_1
            total_amount_nov = sum(list(dict_of_values_for_nov.values()))
            # _______________________________________for december
            amount_for_particular_month(12)
            dict_of_values_for_dec = final_dict_1
            total_amount_dec = sum(list(dict_of_values_for_dec.values()))

            # here we go!
            labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                      'August', 'September', 'October', 'November', 'December']

            sizes = [total_amount_jan, total_amount_feb, total_amount_march, total_amount_april,
                     total_amount_may, total_amount_june, total_amount_july, total_amount_aug,
                     total_amount_sep, total_amount_oct, total_amount_nov, total_amount_dec]
            # explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
            explode = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            explode[cur_month-1] = 0.1
            # explode = (0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2)
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=None, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title(f'Credit Analysis for {cur_year}', bbox={'facecolor': 'yellow', 'pad': 1})
            plt.show()

        def bar_m():              # same as pie_m   just 2 lines difference :)
            date_amount_formatting()
            """Now we have to get all month's date like we did above for just cur month"""
            # _______________________________________for january
            amount_for_particular_month(1)
            dict_of_values_for_jan = final_dict_1
            total_amount_jan = sum(list(dict_of_values_for_jan.values()))
            # _______________________________________for february
            amount_for_particular_month(2)
            dict_of_values_for_feb = final_dict_1
            total_amount_feb = sum(list(dict_of_values_for_feb.values()))
            # _______________________________________for march
            amount_for_particular_month(3)
            dict_of_values_for_march = final_dict_1
            total_amount_march = sum(list(dict_of_values_for_march.values()))
            # _______________________________________for april
            amount_for_particular_month(4)
            dict_of_values_for_april = final_dict_1
            total_amount_april = sum(list(dict_of_values_for_april.values()))
            # _______________________________________for may
            amount_for_particular_month(5)
            dict_of_values_for_may = final_dict_1
            total_amount_may = sum(list(dict_of_values_for_may.values()))
            # _______________________________________for june
            amount_for_particular_month(6)
            dict_of_values_for_june = final_dict_1
            total_amount_june = sum(list(dict_of_values_for_june.values()))
            # _______________________________________for july
            amount_for_particular_month(7)
            dict_of_values_for_july = final_dict_1
            total_amount_july = sum(list(dict_of_values_for_july.values()))
            # _______________________________________for august
            amount_for_particular_month(8)
            dict_of_values_for_aug = final_dict_1
            total_amount_aug = sum(list(dict_of_values_for_aug.values()))
            # _______________________________________for september
            amount_for_particular_month(9)
            dict_of_values_for_sep = final_dict_1
            total_amount_sep = sum(list(dict_of_values_for_sep.values()))
            # _______________________________________for october
            amount_for_particular_month(10)
            dict_of_values_for_oct = final_dict_1
            total_amount_oct = sum(list(dict_of_values_for_oct.values()))
            # _______________________________________for november
            amount_for_particular_month(11)
            dict_of_values_for_nov = final_dict_1
            total_amount_nov = sum(list(dict_of_values_for_nov.values()))
            # _______________________________________for december
            amount_for_particular_month(12)
            dict_of_values_for_dec = final_dict_1
            total_amount_dec = sum(list(dict_of_values_for_dec.values()))

            # here we go!
            labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                      'August', 'September', 'October', 'November', 'December']

            sizes = [total_amount_jan, total_amount_feb, total_amount_march, total_amount_april,
                     total_amount_may, total_amount_june, total_amount_july, total_amount_aug,
                     total_amount_sep, total_amount_oct, total_amount_nov, total_amount_dec]
            plt.bar(labels, sizes)
            plt.xlabel('Months')
            plt.ylabel('Credit Amount')
            plt.title(f'Credit Analysis for {cur_year}', bbox={'facecolor': 'chartreuse', 'pad': 1})
            plt.show()

        def add_bad_debt():
            select_command = "SELECT name FROM records"
            cursor.execute(select_command)
            record_tuple = cursor.fetchall()
            record_list = list(itertools.chain(*record_tuple))

            def store_bd(baddebt_name):
                command = f"SELECT * from records where name = '{baddebt_name}'"
                cursor.execute(command)
                name_tuple = cursor.fetchall()
                name_list = list(itertools.chain(*name_tuple))
                bd_name = name_list[0]   # name
                bd_address = name_list[1]   # address
                bd_phone = name_list[2]    # phone
                bd_amount = name_list[3]    # amount
                bd_date = name_list[4]    # date

                insert_command = "INSERT INTO bad_debts(name,address,phone,amount,date) VALUES(%s,%s,%s,%s,%s)"
                values = (bd_name, bd_address, bd_phone, bd_amount, bd_date)
                cursor.execute(insert_command, values)
                delete_command = f"DELETE FROM records WHERE phone= {bd_phone}"  # phone is our primary key
                cursor.execute(delete_command)
                connection.commit()
                tkinter.messagebox.showinfo('Success!', f'Record "{bd_name}" added to Bad Debts')

            for names in record_list:
                bd_add.add_command(label=f'{names}', command=lambda baddebt_name=names: store_bd(baddebt_name))

        def rec_baddebt():
            select_command = f"SELECT name from bad_debts"
            cursor.execute(select_command)
            record_tuple = cursor.fetchall()
            record_list = list(itertools.chain(*record_tuple))

            def store(baddebt_name):
                command = f"SELECT * from bad_debts where name = '{baddebt_name}'"
                cursor.execute(command)
                name_tuple = cursor.fetchall()
                name_list = list(itertools.chain(*name_tuple))
                bd_name = name_list[0]   # name
                bd_address = name_list[1]   # address
                bd_phone = name_list[2]    # phone
                bd_amount = name_list[3]    # amount
                bd_date = name_list[4]    # date

                insert_command = "INSERT INTO records(name,address,phone,amount,date) VALUES(%s,%s,%s,%s,%s)"
                values = (bd_name, bd_address, bd_phone, bd_amount, bd_date)
                cursor.execute(insert_command, values)
                del_command = f"DELETE from bad_debts where phone = {bd_phone}"
                cursor.execute(del_command)
                connection.commit()

                tkinter.messagebox.showinfo('Success!', f'Record "{bd_name}" Removed From Bad Debts')

            for names in record_list:
                bd_rec.add_command(label=f'{names}', command=lambda baddebt_name=names: store(baddebt_name))

        def ir_credit():
            command_sum = "SELECT amount from bad_debts"  # alternate sum(amount)
            cursor.execute(command_sum)
            amt_tuple = cursor.fetchall()
            amt_list_ir = list(itertools.chain(*amt_tuple))
            ir_credit_amount = sum(amt_list_ir)
            tkinter.messagebox.showinfo('Irrecoverable Amount', f'Irrecoverable Amount is {ir_credit_amount}')
            print(f'Irrecoverable Amount is {ir_credit_amount}')

        def rec_credit():
            command_sum_ = "SELECT amount from records"
            cursor.execute(command_sum_)
            amt_tuple_ = cursor.fetchall()
            amt_list_rec = list(itertools.chain(*amt_tuple_))
            rec_credit_amount = sum(amt_list_rec)
            tkinter.messagebox.showinfo('Recoverable Amount', f'Recoverable Amount is {rec_credit_amount}')
            print(f'Recoverable Amount is {rec_credit_amount}')

        def total_credit():
            # irrecoverable amount calculating here to use it to calculate total amount
            command_sum = "SELECT amount from bad_debts"
            cursor.execute(command_sum)
            amt_tuple = cursor.fetchall()
            amt_list_ir = list(itertools.chain(*amt_tuple))
            ir_credit_amount = sum(amt_list_ir)

            # recoverable amount calculating here to use it to calculate total amount
            command_sum = "SELECT amount from records"
            cursor.execute(command_sum)
            amt_tuple = cursor.fetchall()
            amt_list_rec = list(itertools.chain(*amt_tuple))
            rec_credit_amount = sum(amt_list_rec)

            # total amount = irrecoverable + recoverable
            total_credit_amount = ir_credit_amount + rec_credit_amount
            tkinter.messagebox.showinfo('Total Credit Amount', f'Total Credit Amount is {total_credit_amount}')
            print(f'Total Credit Amount is {total_credit_amount}')

        def records(_event=None):
            rec_screen = Toplevel(root)
            rec_screen.title("Records")
            rec_screen.geometry("1500x600")

            sb_entry = Entry(rec_screen, textvariable=search, width=110, font=('arial', 15))
            sb_entry.grid(row=0, column=0)

            list1 = ['Name', 'Address', 'Phone Number', 'Amount', 'Date']
            records_treeview = ttk.Treeview(rec_screen, column=list1, show='headings', height=30, cursor='hand1')
            scroll_bar = ttk.Scrollbar(rec_screen, orient='vertical', command=records_treeview.yview)
            records_treeview.configure(yscroll=scroll_bar.set)
            scroll_bar.grid(row=1, column=2, sticky='ns')
            for a in list1:
                records_treeview.heading(a, text=a.title())
            records_treeview.grid(row=1, column=0)

            select_command = "SELECT * FROM records"
            cursor.execute(select_command)
            record_tuple = cursor.fetchall()
            record_list = list(itertools.chain(*record_tuple))

            for names in record_list:
                select_command1 = f"SELECT * FROM records WHERE name='{names}'"
                cursor.execute(select_command1)
                record_tuple12 = cursor.fetchall()
                record_list1 = list(itertools.chain(*record_tuple12))
                records_treeview.insert('', 'end', values=record_list1)
            connection.commit()

            def search_(sort_by):
                def sortby_name():  # not working
                    pass

                def sortby_address():
                    pass

                def sortby_phone():
                    pass

                def sortby_amount():
                    pass

                def sortby_date():
                    pass

                searched = search.get()
                parameter = '%' + f'{searched}' + '%'
                if searched != 0:
                    records_treeview.delete(*records_treeview.get_children())
                    command_ = f"SELECT * FROM records WHERE {sort_by} LIKE '{parameter}'"
                    cursor.execute(command_)
                    fetch = cursor.fetchall()
                    for data in fetch:
                        records_treeview.insert('', 'end', values=data)

                """menu button________________________"""
                menu_bar = ttk.Menubutton(rec_screen, text='Sort By', cursor='mouse')
                menu_bar.grid(row=0, column=2)
                menu_ = Menu(menu_bar, tearoff=0)
                menu_bar["menu"] = menu_
                menu_.add_command(label='name', command=sortby_name)
                menu_.add_command(label='address', command=sortby_address)
                menu_.add_command(label='phone', command=sortby_phone)
                menu_.add_command(label='amount', command=sortby_amount)
                menu_.add_command(label='date', command=sortby_date)

            srch_btn = Button(rec_screen, text="Search", bd=1, pady=1, padx=1,
                              relief=RIDGE, overrelief=SUNKEN, cursor='mouse', font=('arial', 12, 'italic'),
                              bg='cyan', command=lambda sort_by="name": search_(sort_by))
            srch_btn.grid(row=0, column=1)
            # rec_screen.bind('<Enter>', lambda sort_by="name": search_(sort_by))

        def update_finally():
            up_name = update_name.get()

            def new_amt():
                select_command__ = f"SELECT phone FROM records WHERE name='{up_name}'"
                cursor.execute(select_command__)
                record_tuple__ = cursor.fetchall()
                record_list_ = list(itertools.chain(*record_tuple__))
                connection.commit()
                primary_key_value = record_list_[0]
                plus_am = plus_amt.get()
                if len(plus_am) == 0:
                    plus_am = 0

                update_command = f"UPDATE records SET amount=amount+{plus_am} WHERE phone = '{primary_key_value}'"
                cursor.execute(update_command)
                connection.commit()
                tkinter.messagebox.showinfo("Success!", "Amount Updated Successfully!")
                up_screen.destroy()

            def amt_rec():
                select_command__ = f"SELECT phone FROM records WHERE name='{up_name}'"
                cursor.execute(select_command__)
                record_tuple__ = cursor.fetchall()
                record_list_ = list(itertools.chain(*record_tuple__))
                connection.commit()
                primary_key_value = record_list_[0]
                minus_amt_ = minus_amt.get()
                if len(minus_amt_) == 0:
                    minus_amt_ = 0

                update_command = f"UPDATE records SET amount=amount-{minus_amt_} WHERE phone = '{primary_key_value}'"
                cursor.execute(update_command)
                connection.commit()
                tkinter.messagebox.showinfo("Success!", "Amount Updated Successfully!")
                up_screen.destroy()

            select_command = f"SELECT * FROM records WHERE name='{up_name}'"
            cursor.execute(select_command)
            record_tuple = cursor.fetchall()
            record_list = list(itertools.chain(*record_tuple))
            connection.commit()

            if len(up_name) == 0:
                tkinter.messagebox.showwarning("Can't Proceed!", "Enter a Record Name!")

            elif up_name in record_list:
                up_screen = Toplevel(root)
                up_screen.title(up_name + "\'s record")
                up_screen.geometry('1100x500')
                text_box1 = Text(up_screen, font=('arial', 10, 'bold'), spacing3=20, fg='snow',
                                 relief=RIDGE, bg='gray2')
                text_box1.config(state='normal')
                text_box1.grid(row=2, column=0)
                # creating dictionary
                keys = ('Name', 'Address', 'Phone', 'Amount', 'Date')
                dict_values = dict(zip(keys, record_list))
                name_ = list(dict_values.keys())[0] + ' : ' + record_list[0]
                address_ = list(dict_values.keys())[1] + ' : ' + record_list[1]
                phone_ = list(dict_values.keys())[2] + ' : ' + record_list[2]
                amount1 = list(dict_values.keys())[3] + ' : ' + str(record_list[3])
                date__ = list(dict_values.keys())[4] + ' : ' + record_list[4]
                value_list = [name_, address_, phone_, amount1, date__]
                for items in value_list:
                    text_box1.insert(END, items + '\n')
                text_box1.config(state='disabled')

                """_________________new amount_____________________"""
                plus_btn = Button(up_screen, text="     New Amount   ", bd=3,
                                  relief=RIDGE, overrelief=SUNKEN, cursor='plus', font=('arial', 15, 'bold', 'italic'),
                                  bg='gold2', command=new_amt)
                plus_btn.grid(row=2, column=1)

                plus_entry = Entry(up_screen, textvariable=plus_amt, width=20,
                                   font=('arial', '25', 'bold'))
                plus_entry.grid(row=2, column=2)
                """_________________amount received_____________________"""
                minus_btn = Button(up_screen, text="Amount Received", bd=3,
                                   relief=RIDGE, overrelief=SUNKEN, cursor='plus', font=('arial', 15, 'bold', 'italic'),
                                   bg='gold2', command=amt_rec)
                minus_btn.grid(row=1, column=1)

                minus_entry = Entry(up_screen, textvariable=minus_amt, width=20,
                                    font=('arial', '25', 'bold'))
                minus_entry.grid(row=1, column=2)
                plus_amt.set("")
                minus_amt.set("")

            else:
                del_name.set("Record does'nt exists")
            update_name.set("")

        def delete_finally():
            delete_name = del_name.get()

            select_command = "SELECT name FROM records"
            cursor.execute(select_command)
            record_tuple = cursor.fetchall()
            record_list = list(itertools.chain(*record_tuple))

            if len(delete_name) == 0:
                tkinter.messagebox.showwarning("Can't Proceed!", "Enter a Record Name!")

            elif delete_name in record_list:
                del_command = f"DELETE FROM records WHERE name='{delete_name}'"
                cursor.execute(del_command)
                connection.commit()
                tkinter.messagebox.showinfo('Success!', f"Record  '{delete_name}'  Deleted Successfully!")
            else:
                del_name.set("Record does'nt exists")
            del_name.set("")

        def save_xlsx(_event=None):          # Not Working
            select_command = "SELECT name FROM records"
            cursor.execute(select_command)
            record_tuple = cursor.fetchall()
            record_list = list(itertools.chain(*record_tuple))
            for names in record_list:
                select_command1 = f"SELECT * FROM records WHERE name='{names}'"
                cursor.execute(select_command1)
                record_tuple1 = cursor.fetchall()
                record_list_ = list(itertools.chain(*record_tuple1))
                keys = ['Name', 'Address', 'Phone', 'Amount', 'Date']
                global final_dict
                final_dict = dict(zip(keys, record_list_))
                global files
                files = [('Microsoft Excel File', '.xlsx')]
            save_path_ = filedialog.asksaveasfilename(filetypes=files, initialdir=cur)
            save_path = str(save_path_) + '.xlsx'

            if save_path:
                writer = pandas.ExcelWriter(save_path, engine='xlsxwriter')
                df = pandas.DataFrame(final_dict, index=[0])
                df.to_excel(writer, sheet_name='Records', index=False)
                writer.save()
            connection.commit()

        def add_finally():
            name = add_name.get()
            address = add_address.get()
            phone = add_phone.get()
            amount = add_amount.get()
            date = add_date.get()
            # list_dirs = os.listdir(cur)
            current_date = datetime.date.today()

            # inserting values to table
            name_ = str(name)
            address_ = str(address)
            phone_ = str(phone)
            try:
                global amount_
                amount_ = float(amount)
            except ValueError:
                tkinter.messagebox.showwarning("Can't Proceed!", 'Amount Must Be A Number')
                add_amount.set('')

            if date == '':
                global date_
                date_ = str(current_date)
            else:
                date_ = date

            if name_ == '':
                tkinter.messagebox.showwarning("Can't Proceed!", 'Every Field Is Necessary')
                add_name.set('')
                add_address.set('')
                add_phone.set('')
                add_amount.set('')
            elif address_ == '':
                tkinter.messagebox.showwarning("Can't Proceed!", 'Every Field Is Necessary')
                add_name.set('')
                add_address.set('')
                add_phone.set('')
                add_amount.set('')
            elif phone_ == '':
                tkinter.messagebox.showwarning("Can't Proceed!", 'Every Field Is Necessary')
                add_name.set('')
                add_address.set('')
                add_phone.set('')
                add_amount.set('')
            elif amount_ == '':
                tkinter.messagebox.showwarning("Can't Proceed!", 'Every Field Is Necessary')
                add_name.set('')
                add_address.set('')
                add_phone.set('')
                add_amount.set('')
            else:
                try:
                    insert_command = "INSERT INTO records(name,address,phone,amount,date) VALUES(%s,%s,%s,%s,%s)"
                    values = (name_, address_, phone_, amount_, date_)
                    cursor.execute(insert_command, values)
                    connection.commit()
                    tkinter.messagebox.showinfo('Success', 'Record Added Successfully!')
                    data = [name_, amount_, date_]
                    recents_treeview.insert('', 'end', values=data)

                except mysql.connector.errors.IntegrityError:
                    tkinter.messagebox.showwarning("Can't Proceed", "Phone Number is already in use!")

                finally:
                    add_name.set('')
                    add_address.set('')
                    add_phone.set('')
                    add_amount.set('')
                    add_date.set('')
                add_screen.destroy()

        def reset(*args):
            for variables in args:
                variables.set('')

        def exit_system(screen):
            if screen == root:
                exit_sys = tkinter.messagebox.askyesno("Exit System?", "Confirm if you want to exit")
                if exit_sys is True:
                    screen.destroy()
            else:
                screen.destroy()

        def update():
            def store_up(upname):
                update_name.set(upname)

            global update_screen
            update_screen = Toplevel(root)
            update_screen.title("Update Record")
            update_screen.geometry("900x500")

            # ignore frames (pretty wasting of lines for formatting)
            main_frame___ = Frame(update_screen, bd=10)
            main_frame___.grid()

            top___ = Frame(main_frame___, bd=10, width=100, relief=RIDGE)
            top___.pack(side=TOP)

            up_ent_frame = LabelFrame(main_frame___, bd=10, width=500, height=150, font=('helvetica', 20, 'bold'),
                                      relief=RIDGE)
            up_ent_frame.pack(side=TOP)

            up_but_frame = LabelFrame(main_frame___, bd=10, width=700, height=400, font=('helvetica', 20, 'bold'),
                                      relief=RIDGE)
            up_but_frame.pack(side=BOTTOM)

            up_name = Label(top___, text="Update Record", font=('arial', 30, 'bold'),
                            padx=2, pady=2, bd=2)
            up_name.grid(row=0, column=0)

            """____________________________name____________________________________"""
            lbl_name = Label(up_ent_frame, text="Debtor Name:", font=('arial', 15, 'bold'),
                             padx=2, pady=2, bd=2)
            lbl_name.grid(row=1, column=0)

            entry_name = Entry(up_ent_frame, width=40, textvariable=update_name, font=('arial', 15, 'bold'),
                               cursor='xterm')
            entry_name.grid(row=1, column=1)
            """menu button________________________"""
            menu_bar = ttk.Menubutton(up_ent_frame, text='names', cursor='mouse')
            menu_bar.grid(row=1, column=2)
            """________menu of menubutton_________________________"""
            menu_ = Menu(menu_bar, tearoff=0)
            menu_bar["menu"] = menu_

            select_command = "SELECT name FROM records"
            cursor.execute(select_command)
            record_tuple = cursor.fetchall()
            record_list = list(itertools.chain(*record_tuple))

            for names in record_list:
                menu_.add_command(label=f'{names}', command=lambda upname=names: store_up(upname))

            """________________________________btns___________________________________"""
            add_btn = Button(up_but_frame, text="Update", bd=3, pady=1, padx=1,
                             relief=RIDGE, overrelief=SUNKEN, cursor='plus', font=('arial', 20, 'bold', 'italic'),
                             bg='gold2', command=update_finally)
            add_btn.grid(row=2, column=0)

            add_btn = Button(up_but_frame, text=" Reset ", bd=3, pady=1, padx=1,
                             relief=RIDGE, overrelief=SUNKEN, cursor='hand1', font=('arial', 20, 'bold', 'italic'),
                             bg='gold2', command=lambda: reset(update_name))
            add_btn.grid(row=2, column=1)

            add_btn = Button(up_but_frame, text="   Exit  ", bd=3, pady=1, padx=1,
                             relief=RIDGE, overrelief=SUNKEN, cursor='pirate', font=('arial', 20, 'bold', 'italic'),
                             bg='gold2', command=lambda screen=update_screen: exit_system(screen))
            add_btn.grid(row=2, column=2)
            update_name.set("")

        def delete_record():

            def store_del(delname):
                del_name.set(delname)

            global del_screen
            del_screen = Toplevel(root)
            del_screen.title('Delete Record')
            del_screen.geometry('900x500')
            # ignore frames (pretty wasting of lines for formatting)
            main_frame__ = Frame(del_screen, bd=10)
            main_frame__.grid()

            top__ = Frame(main_frame__, bd=10, width=100, relief=RIDGE)
            top__.pack(side=TOP)

            del_ent_frame = LabelFrame(main_frame__, bd=10, width=500, height=150, font=('helvetica', 20, 'bold'),
                                       relief=RIDGE)
            del_ent_frame.pack(side=TOP)

            del_but_frame = LabelFrame(main_frame__, bd=10, width=700, height=400, font=('helvetica', 20, 'bold'),
                                       relief=RIDGE)
            del_but_frame.pack(side=BOTTOM)

            lbl_name = Label(top__, text="Delete Record", font=('arial', 30, 'bold'),
                             padx=2, pady=2, bd=2)
            lbl_name.grid(row=0, column=0)
            """____________________________name____________________________________"""
            lbl_name = Label(del_ent_frame, text="Debtor Name:", font=('arial', 15, 'bold'),
                             padx=2, pady=2, bd=2)
            lbl_name.grid(row=1, column=0)

            entry_name = Entry(del_ent_frame, width=40, textvariable=del_name, font=('arial', 15, 'bold'),
                               cursor='xterm')
            entry_name.grid(row=1, column=1)

            menu_bar = ttk.Menubutton(del_ent_frame)
            menu_bar.grid(row=1, column=2)
            """menu button________________________"""
            menu_bar = ttk.Menubutton(del_ent_frame, text='names', cursor='mouse')
            menu_bar.grid(row=1, column=2)
            """________menu of menubutton_________________________"""
            menu_ = Menu(menu_bar, tearoff=0)
            menu_bar["menu"] = menu_

            select_command = "SELECT name FROM records"
            cursor.execute(select_command)
            record_tuple = cursor.fetchall()
            record_list = list(itertools.chain(*record_tuple))

            for names in record_list:
                menu_.add_command(label=f'{names}', command=lambda delname=names: store_del(delname))
            """________________________________btns___________________________________"""
            add_btn = Button(del_but_frame, text=" Delete", bd=3, pady=1, padx=1,
                             relief=RIDGE, overrelief=SUNKEN, cursor='spider', font=('arial', 20, 'bold', 'italic'),
                             bg='gold2', command=delete_finally)
            add_btn.grid(row=2, column=0)

            add_btn = Button(del_but_frame, text=" Reset ", bd=3, pady=1, padx=1,
                             relief=RIDGE, overrelief=SUNKEN, cursor='hand1', font=('arial', 20, 'bold', 'italic'),
                             bg='gold2', command=lambda: reset(del_name))
            add_btn.grid(row=2, column=1)

            add_btn = Button(del_but_frame, text="   Exit  ", bd=3, pady=1, padx=1,
                             relief=RIDGE, overrelief=SUNKEN, cursor='pirate', font=('arial', 20, 'bold', 'italic'),
                             bg='gold2', command=lambda screen=del_screen: exit_system(screen))
            add_btn.grid(row=2, column=2)

        def add_record():
            def date_picker():
                def select_date():
                    selected_date = cal.selection_get()    # YEAR MONTH DAY
                    add_date.set(selected_date)
                    cal_window.destroy()
                cal_window = Toplevel(root)
                cal_window.title('Calendar')
                cal_window.geometry('260x250+100+100')
                cal = Calendar(cal_window, selectmode="day", year=cur_year, month=cur_month, day=cur_day,
                               cursor='hand1')
                cal.grid(row=0, column=0, padx=3, pady=3)
                pick_btn = Button(cal_window, text='Select', command=select_date)
                pick_btn.grid(row=1, column=0)

            global add_screen
            add_screen = Toplevel(root)
            add_screen.title("Add new record")
            add_screen.geometry("800x500")
            # ignore frames (pretty wasting of lines for formatting)
            main_frame_ = Frame(add_screen, bd=10)
            main_frame_.grid()

            top_ = Frame(main_frame_, bd=10, width=100, relief=RIDGE)
            top_.pack(side=TOP)

            add_ent_frame = LabelFrame(main_frame_, bd=10, width=500, height=150, font=('helvetica', 20, 'bold'),
                                       relief=RIDGE)
            add_ent_frame.pack(side=TOP)

            add_but_frame = LabelFrame(main_frame_, bd=10, width=700, height=400, font=('helvetica', 20, 'bold'),
                                       relief=RIDGE)
            add_but_frame.pack(side=BOTTOM)

            lbl_name = Label(top_, text="Add Record", font=('arial', 30, 'bold'),
                             padx=2, pady=2, bd=2)
            lbl_name.grid(row=0, column=0)
            """____________________________name____________________________________"""
            lbl_name = Label(add_ent_frame, text="Debtor Name:", font=('arial', 15, 'bold'),
                             padx=2, pady=2, bd=2)
            lbl_name.grid(row=1, column=0)

            entry_name = Entry(add_ent_frame, width=40, textvariable=add_name, font=('arial', 15, 'bold'),
                               cursor='xterm')
            entry_name.grid(row=1, column=1)
            """____________________________address____________________________________"""

            lbl_name = Label(add_ent_frame, text="Debtor Address:", font=('arial', 15, 'bold'),
                             padx=2, pady=2, bd=2)
            lbl_name.grid(row=2, column=0)

            entry_name = Entry(add_ent_frame, width=40, textvariable=add_address, font=('arial', 15, 'bold'),
                               cursor='xterm')
            entry_name.grid(row=2, column=1)
            """____________________________phone____________________________________"""

            lbl_name = Label(add_ent_frame, text="Phone Number *:", font=('arial', 15, 'bold'),
                             padx=2, pady=2, bd=2)
            lbl_name.grid(row=3, column=0)

            entry_name = Entry(add_ent_frame, width=40, textvariable=add_phone, font=('arial', 15, 'bold'),
                               cursor='xterm')
            entry_name.grid(row=3, column=1)
            """____________________________amount____________________________________"""

            lbl_name = Label(add_ent_frame, text="Amount ₹:", font=('arial', 15, 'bold'),
                             padx=2, pady=2, bd=2)
            lbl_name.grid(row=4, column=0)

            entry_name = Entry(add_ent_frame, width=40, textvariable=add_amount, font=('arial', 15, 'bold'),
                               cursor='xterm')
            entry_name.grid(row=4, column=1)
            """____________________________date____________________________________"""

            lbl_name = Label(add_ent_frame, text="Date", font=('arial', 15, 'bold'),
                             padx=2, pady=2, bd=2)
            lbl_name.grid(row=5, column=0)

            entry_name = Entry(add_ent_frame, width=40, textvariable=add_date, font=('arial', 15, 'bold'),
                               cursor='xterm')
            entry_name.config(state='disabled')      # so that date format must be followed
            entry_name.grid(row=5, column=1)
            cal_btn = Button(add_ent_frame, text="📆", bd=3, pady=1, padx=1,
                             font=('arial', 20, 'bold'), relief=FLAT, overrelief=RIDGE,
                             command=date_picker)
            cal_btn.grid(row=5, column=2)
            """________________________________btns___________________________________"""
            add_btn = Button(add_but_frame, text=" Add  ", bd=3, pady=1, padx=1,
                             relief=RIDGE, overrelief=SUNKEN, cursor='plus', font=('arial', 20, 'bold', 'italic'),
                             bg='gold2', command=add_finally)
            add_btn.grid(row=6, column=0)

            add_btn = Button(add_but_frame, text="Reset", bd=3, pady=1, padx=1,
                             relief=RIDGE, overrelief=SUNKEN, cursor='hand1', font=('arial', 20, 'bold', 'italic'),
                             bg='gold2',
                             command=lambda: reset(add_name, add_address, add_phone, add_date, add_amount))
            add_btn.grid(row=6, column=1)

            add_btn = Button(add_but_frame, text=" Exit  ", bd=3, pady=1, padx=1,
                             relief=RIDGE, overrelief=SUNKEN, cursor='pirate', font=('arial', 20, 'bold', 'italic'),
                             bg='gold2', command=lambda screen=add_screen: exit_system(screen))
            add_btn.grid(row=6, column=2)

        """___________________________________________________________________frames"""
        main_frame = Frame(self.root, bd=10)
        main_frame.grid()

        top = Frame(main_frame, bd=10, width=100, relief=RIDGE)
        top.pack(side=TOP)

        recent_frame = LabelFrame(main_frame, bd=10, width=700, height=400, font=('helvetica', 20, 'bold'),
                                  relief=RIDGE)
        recent_frame.pack(side=BOTTOM, fill=X)

        button_frame = LabelFrame(main_frame, bd=10, width=500, height=150, font=('helvetica', 20, 'bold'),
                                  relief=RIDGE)
        button_frame.pack(side=TOP)

        """__________________top frame_____________________"""
        self.lbl1 = Label(top, font=('helvetica', 31, 'bold'), text='Khata Book',
                          justify=CENTER, bg='gold1', cursor='sailboat')
        self.lbl1.grid(row=0, column=0)

        """______________________button_frame________________________"""
        global add_button
        add_button = Button(button_frame, text="Add record", bd=6, pady=3, padx=3,
                            relief=RIDGE, overrelief=SOLID, cursor='plus', font=('arial', 20, 'bold', 'italic'),
                            command=add_record)
        add_button.grid(row=0, column=0)
        global del_button
        del_button = Button(button_frame, text="Delete record", bd=6, pady=3, padx=3,
                            relief=RIDGE, overrelief=SOLID, cursor='pirate', font=('arial', 20, 'bold', 'italic'),
                            command=delete_record)
        del_button.grid(row=0, column=1)
        global update_button
        update_button = Button(button_frame, text="Update record", bd=6, pady=3, padx=3,
                               relief=RIDGE, overrelief=SOLID, cursor='spider', font=('arial', 20, 'bold', 'italic'),
                               command=update)
        update_button.grid(row=0, column=2)

        """__________________recent_frame______________________________"""
        self.lbl = Label(recent_frame, font=('arial', 15, 'bold'), text='Recent records:',
                         justify=CENTER)
        self.lbl.grid(row=0, column=0)

        recents = ['Name', 'Amount', 'Date']
        recents_treeview = ttk.Treeview(recent_frame, column=recents, show='headings', height=9, cursor='hand1')
        scroll_bar1 = ttk.Scrollbar(recent_frame, orient='vertical', command=recents_treeview.yview)
        recents_treeview.configure(yscroll=scroll_bar1.set)
        scroll_bar1.grid(row=1, column=2, sticky='ns')
        for i in recents:
            recents_treeview.heading(i, text=i.title())
        recents_treeview.grid(row=1, column=0)

        lbl4 = Label(recent_frame, text="© Copyright : Vanshu Galhotra", font=('helvetica', 9, 'bold'),
                     bd=2)
        lbl4.grid(row=2, column=0)

        """_____________________________--menu bar__--____________________________________________"""

        """________________menu______________________________"""
        main_menu = Menu(root)
        root.configure(menu=main_menu)
        file_sub = Menu(main_menu)
        record_sub = Menu(file_sub)
        sub_menu = Menu(file_sub)
        save_sub = Menu(file_sub)
        tool_sub = Menu(file_sub)
        credit_sub = Menu(tool_sub)
        # setting_sub = Menu(file_sub)
        baddebt_menu = Menu(tool_sub)
        global bd_add
        bd_add = Menu(baddebt_menu)
        global bd_rec
        bd_rec = Menu(baddebt_menu)
        graph_sub = Menu(tool_sub)
        hist_sub = Menu(graph_sub)
        pie_sub = Menu(graph_sub)
        bar_sub = Menu(graph_sub)

        main_menu.add_cascade(label="File", menu=file_sub)  # m1
        file_sub.add_cascade(label="Records", menu=record_sub)  # f1
        record_sub.add_command(label='All (Ctrl-Alt-a)', command=records)  # f1r1
        root.bind('<Control-Alt-a>', records)
        record_sub.add_command(label='Bad debts')      # f1r2
        file_sub.add_cascade(label="Save record", menu=save_sub)   # f2
        save_sub.add_command(label='Excel sheet (Ctrl-s)', command=save_xlsx)  # f2r1
        root.bind('<Control-s>', save_xlsx)
        save_sub.add_command(label='Text file')               # f2r2
        file_sub.add_command(label="Exit", command=lambda screen=root: exit_system(screen))  # f3

        main_menu.add_cascade(label="Tools", menu=tool_sub)     # m2
        tool_sub.add_cascade(label='credit', menu=credit_sub)   # t1
        credit_sub.add_command(label='Total (Ctrl-Alt-t)', command=total_credit)     # t1c1
        root.bind('<Control-Alt-t>', total_credit)
        credit_sub.add_command(label='Irrecoverable', command=ir_credit)         # t1c2
        credit_sub.add_command(label='Recoverable', command=rec_credit)            # t1c3
        tool_sub.add_cascade(label='Bad debts', menu=baddebt_menu)   # t2
        baddebt_menu.add_cascade(label='Add', menu=bd_add)              # t2b1
        add_bad_debt()
        baddebt_menu.add_cascade(label='Recoverable', menu=bd_rec)       # t2b2
        rec_baddebt()
        tool_sub.add_cascade(label='Graph', menu=graph_sub)    # t3

        graph_sub.add_cascade(label='Pie chart', menu=pie_sub)                # t3g1
        pie_sub.add_cascade(label='This year', command=pie_m)                # t3g1

        graph_sub.add_cascade(label='Time-Series', menu=hist_sub)      # t3g2
        hist_sub.add_command(label='Last 7 Days', command=show_ts_ls)
        hist_sub.add_command(label='This Month', command=show_ts_lm)
        hist_sub.add_command(label='Specify*')

        graph_sub.add_cascade(label='Bar Graph', menu=bar_sub)                # t3g1
        bar_sub.add_cascade(label='This Year', command=bar_m)

        main_menu.add_cascade(label="Help", menu=sub_menu)
        sub_menu.add_command(label='Information (Ctrl-i)')
        root.bind('<Control-i>')
        sub_menu.add_command(label="About Us  (Ctrl-u)", command=au)
        root.bind('<Control-u>', au)
        sub_menu.add_command(label="GitHub Repository", command=git_repo)

        """__________________top frame_____________________"""
        self.lbl1 = Label(top, font=('helvetica', 31, 'bold'), text='Khata Book',
                          justify=CENTER, bg='gold1', cursor='sailboat')
        self.lbl1.grid(row=0, column=0)


if __name__ == '__main__':
    root = Tk()
    application = KhataBook()
    root.mainloop()
