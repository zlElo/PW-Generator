package de.zlelo.pwgen.tools
import kotlin.text.StringBuilder

class Generator {
    companion object {
        private const val LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        private const val NUMBERS = "1234567890"
        private const val SPECIAL = "!%&/()$@=?+*#-_.:,;<>^"
        fun generate(lettersVal: Boolean, numberVal: Boolean, specialVal: Boolean, count: Int): String {
            val stringBuilder = StringBuilder()
            val pw = StringBuilder()

            // check if all false
            if (listOf(lettersVal, numberVal, specialVal).all { !it }) {
                return "Please select characters!"
            }

            // append all symbols, numbers and letters
            if (lettersVal) {
                stringBuilder.append(LETTERS)
            }
            if (numberVal) {
                stringBuilder.append(NUMBERS)
            }
            if (specialVal) {
                stringBuilder.append(SPECIAL)
            }

            for (i in 1.. count) {
                pw.append(stringBuilder.random())
            }

            return pw.toString()
        }
    }
}