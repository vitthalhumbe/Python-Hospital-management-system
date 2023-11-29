from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+8+8")

        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEfect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        lbltitle = Label(self.root, bd=10, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white",font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        Dataframe = Frame(self.root, bd=10, relief=RIDGE)
        Dataframe.place(x=0, y=100, width=1530, height=390)

        Dataframeleft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=18, font=("times new roman", 12, "bold"),text="Patient Information")
        Dataframeleft.place(x=8, y=5, width=980, height=358)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=18, font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=998, y=5, width=490, height=357)

        Buttonframe = Frame(self.root, bd=10, relief=RIDGE)
        Buttonframe.place(x=0, y=490, width=1530, height=60)

        Detailsframe = Frame(self.root, bd=10, relief=RIDGE)
        Detailsframe.place(x=0, y=545, width=1530, height=290)

        lblNameTablet = Label(Dataframeleft, text="Names of Tablet", font=("times new roman", 12, 'bold'), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(Dataframeleft, textvariable=self.Nameoftablets, font=("times new roman", 12, "bold"), width=33)
        comNametablet["values"] = ("Nice", "Corona Vacacine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.grid(row=0, column=1)

        lblref = Label(Dataframeleft, font=("arial", 12, "bold"), text="reference no. :", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(Dataframeleft, textvariable=self.ref, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(Dataframeleft, font=("arial", 12, "bold"), text="Dose:", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(Dataframeleft, textvariable=self.Dose, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)

    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="username", password="password", database="database_name")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO patientdata VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()
            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success", "Successfully added data !")

    def update_data(self):
        conn = mysql.connector.connect(host="localhost", username="username", password="password", database="database_name")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE patientdata SET Nameoftablets=%s, dose=%s, NumbersofTablets=%s,  lot=%s, "
                          "issuedate=%s, expdate=%s, dailydose=%s, nhsnumber=%s, patientname=%s,  DOB=%s, "
                          "patientaddress=%s WHERE Reference_No=%s",
                          (
                              self.Nameoftablets.get(),
                              self.Dose.get(),
                              self.NumberofTablets.get(),
                              self.Lot.get(),
                              self.Issuedate.get(),
                              self.ExpDate.get(),
                              self.DailyDose.get(),
                              self.nhsNumber.get(),
                              self.PatientName.get(),
                              self.DateOfBirth.get(),
                              self.PatientAddress.get(),
                              self.ref.get()
                          ))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Successfully updated data !")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="username", password="password", database="database_name")
        my_cursor = conn.cursor()
        my_cursor.execute('SELECT * FROM patientdata')
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()

        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrectioption(self):
        self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose: \t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number Of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot: \t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect:\t\t\t" + self.sideEfect.get() + "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END, "StorageAdvice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, " PatientId:\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END, "NHSNumber: \t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "PatientName:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "DateOfBirth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "PatientAddress:\t\t\t" + self.PatientAddress.get() + "\n")

    def idelete(self):
        conn = mysql.connector.connect(host="localhost", username="username", password="password", database="database_name")
        my_cursor = conn.cursor()
        query = 'DELETE FROM patientdata WHERE Reference_No=%s'
        value = (self.ref.get(),)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fatch_data()
        messagebox.showinfo('Delete', 'Patient has been deleted successfully !')

    def iclear(self):
        self.Nameoftablets.set('')
        self.ref.set('')
        self.Dose.set('')
        self.NumberofTablets.set('')
        self.Lot.set('')
        self.Issuedate.set('')
        self.ExpDate.set('')
        self.DailyDose.set('')
        self.sideEfect.set('')
        self.FurtherInformation.set('')
        self.StorageAdvice.set('')
        self.HowToUseMedication.set('')
        self.PatientId.set('')
        self.nhsNumber.set('')
        self.PatientName.set('')
        self.DateOfBirth.set('')
        self.PatientAddress.set('')

    def iexit(self):
        iExit = messagebox.askyesno('Hospital Management System', 'Confirm you want to exit', parent=self.root)
        if iExit > 0:
            win.destroy()
            return

win = Tk()
ob = Hospital(win)
win.mainloop()
