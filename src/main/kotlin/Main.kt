import androidx.compose.desktop.ui.tooling.preview.Preview
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.padding
import androidx.compose.material.*
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.WindowState
import androidx.compose.ui.window.application
import androidx.compose.ui.unit.dp
import de.zlelo.pwgen.tools.Generator

@Composable
@Preview
fun App() {
    MaterialTheme {
        // Main GUI
        val lettersCheck = remember { mutableStateOf(false) }
        val numberCheck = remember { mutableStateOf(false) }
        val specialCheck = remember { mutableStateOf(false) }
        val sliderPosition = remember { mutableFloatStateOf(10f) }
        val pw = remember { mutableStateOf("") }

        Column (
            Modifier.padding(horizontal = 16.dp)
        ) {
            // GUI Row
            Row (
                verticalAlignment = Alignment.CenterVertically
            ) {
                // Letters
                Text(
                    text = "Letters",
                )

                Checkbox(
                    checked = lettersCheck.value,
                    onCheckedChange = { lettersCheck.value = it }
                )

                // Numbers
                Text(
                    text = "Numbers",
                )

                Checkbox(
                    checked = numberCheck.value,
                    onCheckedChange = { numberCheck.value = it }
                )

                // Specials
                Text(
                    text = "Specials",
                )

                Checkbox(
                    checked = specialCheck.value,
                    onCheckedChange = { specialCheck.value = it }
                )
            }

            Slider(
                value = sliderPosition.value,
                onValueChange = { sliderPosition.value = it },
                valueRange = (1f .. 25f)
            )

            Row {
                Column {
                    Text(text = "Length: ${sliderPosition.value.toInt()}") // Show selected value

                    Button(onClick = {pw.value = Generator.generate(lettersCheck.value, numberCheck.value, specialCheck.value, sliderPosition.value.toInt())}) {
                        Text("Generate")
                    }
                }
                Column(
                    Modifier.padding(horizontal = 20.dp, vertical = 8.dp)
                ) {
                    TextField(
                        onValueChange = { },
                        value = pw.value
                    )
                }
            }
        }
    }
}

fun main() = application {
    Window(onCloseRequest = ::exitApplication, state = WindowState(width = 500.dp, height = 230.dp), resizable = false, title = "PW-Generator") {
        App()
    }
}
