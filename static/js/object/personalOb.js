let titleState = class {
    constructor() {
        this.unsaved = 1
        this.saved = 0
    }
}

class Concept {
    constructor (title=titleState, summary='') {
        this.title = title
        this.summary = summary
    }
}


