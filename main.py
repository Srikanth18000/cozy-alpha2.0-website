from flask import Flask, request, render_template, redirect
import openai

openai.api_key = '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'

app = Flask(__name__)

def send_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]['message']['content']
    except Exception as e:
        return e


@app.route('/', methods=['GET', 'POST'])
def get_request_json():
    if request.method == 'POST':
        if len(request.form['question']) < 1:
            return render_template(
                'chat3.5.html', question="NULL", res="Question can't be empty!")
        question = request.form['question']
        print("======================================")
        print("Receive the question:", question)
        res = send_gpt(question)
        print("Q：\n", question)
        print("A：\n", res)

        return render_template('chat3.5.html', question=question, res=str(res))
    return render_template('chat3.5.html', question=0)

if __name__ == '__main__':
    app.run(debug=True)
