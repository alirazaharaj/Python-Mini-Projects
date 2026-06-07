from tkinter import *
import speedtest
import threading

def speed():
    try:
        # Disable button during test
        Shut.config(state=DISABLED, text="Testing...")
        
        def run_test():
            try:
                st = speedtest.Speedtest()
                st.get_servers()
                st.get_best_server()
                
                # Test download and upload
                download = st.download() / 10**6  # Convert to Mbps
                upload = st.upload() / 10**6      # Convert to Mbps
                
                # Update UI with results
                la_Down.config(text=f"{download:.3f} Mbps")
                la_Upload.config(text=f"{upload:.3f} Mbps")
                
            except Exception as e:
                la_Down.config(text="Error")
                la_Upload.config(text=str(e))
            finally:
                # Re-enable button
                Shut.config(state=NORMAL, text="Speed Check")
        
        # Run speed test in a separate thread to avoid freezing the UI
        threading.Thread(target=run_test, daemon=True).start()
        
    except Exception as e:
        la_Down.config(text="Error")
        la_Upload.config(text=str(e))
        Shut.config(state=NORMAL, text="Speed Check")

app = Tk()
app.title('Network Speed Tester')
app.geometry('400x650')
app.config(bg='white')

# Create and pack all your widgets as before
la_name = Label(app, text='Network Speed Tester', font=('Lucida Handwriting', 25, 'bold'), bg='white')
la_name.pack(pady=10)

la_Show = Label(app, text='Downloading Speed', font=('Times New Roman', 20), bg='white')
la_Show.pack(pady=(90,0))

la_Down = Label(app, text='00', font=('Times New Roman', 20), 
               width=10, highlightthickness=4, highlightbackground='#007bff', bg='#f8f9fa')
la_Down.pack(pady=10)

la_Show1 = Label(app, text='Uploading Speed', font=('Times New Roman', 20), bg='white')
la_Show1.pack(pady=(90,0))

la_Upload = Label(app, text='00', font=('Times New Roman', 20), 
                 width=10, highlightthickness=4, highlightbackground='#007bff', bg='#f8f9fa')
la_Upload.pack(pady=10)

Shut = Button(app, text='Speed Check', font=('Lucida Handwriting', 15, 'bold'), 
              relief=RAISED, command=speed)
Shut.pack(pady=(70,0))

app.mainloop()
