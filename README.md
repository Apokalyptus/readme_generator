# Projektanalyse

```markdown
# Code Analyse und Dokumentationsgenerierung mit Ollama

Dieses Projekt automatisiert die Analyse von Code-Dateien und generiert daraus eine umfassende Dokumentation in Form einer `README.md` Datei. Es nutzt Ollama, ein lokales LLM (Large Language Model) Server, um die Code-Dateien zu verstehen und zu dokumentieren.

## Was ist das Projekt und was kann ich damit machen?

Das Projekt hilft Ihnen, bestehenden Code-Projekten schnell eine strukturierte Dokumentation zu erstellen.  Es skaliert für größere Projekte, indem es die Analyse in kleinere Teile aufteilt, um die Effizienz zu steigern. Das Ergebnis ist eine `README.md` Datei, die Ihnen hilft, den Zweck, die Struktur und die wichtigsten Funktionen des Projekts schnell zu verstehen.

## Wie funktioniert das?

1.  **Code-Scan:** Das Projekt durchsucht Ihr Projektverzeichnis nach Code-Dateien (z.B. `.py` Dateien).
2.  **Chunking:** Große Code-Dateien werden in kleinere Abschnitte (Chunks) aufgeteilt, um die Verarbeitung durch Ollama zu erleichtern.
3.  **Ollama Analyse:** Jeder Chunk wird an Ollama gesendet, um eine kurze Zusammenfassung zu erhalten.
4.  **Zusammenführung:** Alle Zusammenfassungen werden zu einer einzigen, umfassenden Zusammenfassung für jede Code-Datei zusammengefügt.
5.  **README Generierung:** Aus diesen Zusammenfassungen wird automatisch eine strukturierte `README.md` Datei erstellt.

## Für wen ist das Projekt gedacht?

Dieses Projekt ist ideal für:

*   **Entwickler:** Die schnell eine Übersicht über ein bestehendes Projekt erhalten möchten, ohne jedes einzelne Code-File durchlesen zu müssen.
*   **Teammitglieder:** Die den Überblick über ein Projekt gewinnen müssen, insbesondere wenn sie neu im Projekt sind.
*   **Projektinfrastruktur:** Die automatisiert eine grundlegende Dokumentation für neue Projekte oder solche, die eine schnellere Auffrischung der Dokumentation benötigen.

## Installation und Verwendung (nicht im Detail beschrieben, siehe Code-Ausschnitt)

(Hier würden Sie eine kurze Anleitung zur Installation und Verwendung des Projekts geben. Dies würde die Abhängigkeiten auflisten, die Installation beschreiben und eine kurze Verwendungshilfe geben. Da die Aufgaben sich auf die Code-Verarbeitung konzentrieren, wird dies hier kurz gehalten.)

## Weitere Informationen

(Hier könnten Sie Links zu Dokumentation, Demos oder anderen relevanten Ressourcen hinzufügen.)
```
