import "./style.scss"
import { useRef } from "react"
import emailjs from '@emailjs/browser'

import { toast } from 'react-toastify';

function Email(props) {

    const form = useRef() // reference to the form element

    const submit = (e) => {
        e.preventDefault() // prevents the page from reloading when you hit “Send”

        emailjs.sendForm('service_8aytxhp', 'template_dbx4qji', form.current, 'mbcCG18ZiPltCRfB-')
            .then((result) => {
                toast.success("Message Sent", {theme: "dark"})
                // alert('Message Sent', result.text)
                // show the user a success message
            }, (error) => {
                toast.error("An error occurred, Please try again", {theme: "dark"})
                // alert('An error occurred, Please try again', error.text)
                // show the user an error
            })

        e.target.reset() // resets the form after submission
    }

    return (
        <div className="email-form-wrapper">
            <h1>Send Email</h1>

            <form ref={form} onSubmit={(e) => submit(e)}>
                <input type="text" placeholder='Напишите своё имя' name='from_name' />

                <label htmlFor="exampleInputEmail1">Email address</label>
                <input type="email" id="exampleInputEmail1"
                    placeholder="Reciever email address" name='from_email'
                />
                <small id="email-help">
                    We'll never share your email with anyone else.
                </small>

                <label htmlFor="exampleFormControlTextarea1">Message</label>
                <textarea id="exampleFormControlTextarea1" rows="3" cols="20"
                    placeholder="Enter your message here..."
                    name="message"
                ></textarea>
                <small id="message-help">Text area for your message.</small>

                <button type="submit">Submit</button>
            </form>
        </div>
    )
}

export default Email;